import socket


def tcp_check_connect(str_host, int_port):
    """
    do a TCP connect on int_port to str_host
    :param str_host: fqdn or IP address
    :param int_port: portnumber
    :return: True on success, False on failure
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((str_host, int_port))
    if result == 0:
        return True
    else:
        return False

print(tcp_check_connect('domoticz.local', 8080))

