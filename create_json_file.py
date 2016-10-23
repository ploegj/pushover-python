import json

user = input('User :')
token = input('Token :')

list = {'user':user, 'token':token}

with open('pushover.json','w') as outfile:
    json.dump(list,outfile, indent=4)

with open('pushover.json','r') as infile:
    str_json_in = json.load(infile)

print('json-str :',str_json_in)