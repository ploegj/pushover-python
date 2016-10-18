import requests
import sys


class Pushover(object):
    """
    creates an object to send messages through the pushover service
    see https://pushover.net/api for info
    """
    def __init__(self, str_user, str_token):
        self.user = str_user
        self.token = str_token
        self.pushover_session = requests.session()
        self.validated = False

    def check_connectivity(self):
        """
        check if the provided user and token are valid
        :return: True and set validated to True if connectivity has been checked
        """
        payload = {
            "token": self.token,
            "user": self.user,
        }
        r = self.pushover_session.post('https://api.pushover.net/1/users/validate.json', data=payload)
        if not r.status_code == requests.codes.ok:
            # r_json = r.json().
            # r_json["status"].
            return False
        else:
            # r_json = r.json().
            # r_json["status"].
            self.validated = True
            return True

    def send_message(self, str_title, str_message, int_priority=0, str_sound='pushover'):
        ''' Send a message through the pushover service
        :param str_title:
        :param str_message:
        :param int_priority:
         priority ranges between -2 and 2, -1 and -2 will not affect in sound
         1 sounds during users quiet hours
         2 sounds until the notification is acknowledged by the user
        :param str_sound: check https://pushover.net/api#sounds for the available sounds
        :return: True if message was accepted.
        '''
        if not self.validated:
            return False
        payload = {
            "token": self.token,
            "user": self.user,
            "title": str_title,
            "message": str_message,
            "priority": priority,
            "sound": sound,
        }
        r = requests.post("https://api.pushover.net/1/messages.json", data=payload)
        if not r.status_code == requests.codes.ok:
            return False
        else:
            return True


if __name__ == '__main__':
    import os
    import pickle

    data_loaded = False
    # For ease of use or testing you can save the user and token in a pickle
    script_path = os.path.dirname(sys.argv[0])
    pickle_file = 'pushover.pickle'
    if os.path.isfile(script_path + '/' + pickle_file):
        with open(script_path + '/' + pickle_file, 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            pushover_data = pickle.load(f)
            print('type ;', type(pushover_data))
            data_loaded = True

    if data_loaded is True:
        user = pushover_data['user']
        token = pushover_data['token']
        print('user :', user)
        print('token :', token)
    else:
        user = input('Enter pushover user :')
        token = input('Enter pushover token :')
        if (len(user) == 0) or (len(token) == 0):
            sys.exit("user or token is empty")

    'initialize my_pushover'
    my_pushover = Pushover(str_user=user, str_token=token)
    'validate user and token'
    if not my_pushover.check_connectivity():
        sys.exit('invalid token or user')
    else:
        print('valid user')

    print(my_pushover.send_message(str_title='', str_message='message 4', int_priority=-1))
