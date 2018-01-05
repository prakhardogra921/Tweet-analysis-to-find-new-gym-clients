__author__ = 'prakhardogra'

import json
import time
from download_tweets import download_tweets

download_tweets()

time.sleep(5)

with open("users.json", 'r') as f:
    users = json.load(f)
#print users
all_users = []
all_names = []
for user in users:
    if user['user_name'] not in all_users:
        all_users.append(user['user_name'])
        all_names.append(user['name'])
    if user['user_mention']:
        mentioned_user = user['user_mention'][0]['screen_name']
        if mentioned_user not in all_users:
            all_users.append(mentioned_user)
            all_names.append(user['user_mention']['name'])

f = open('users.csv','a')

for i in range(len(all_users)):
    row = all_users[i] + "," + all_names[i] + "\n"
    #row = all_users[i]+"\n"
    f.write(row)
f.close()

time.sleep(5)

f = open("users.csv","r+")
for row in f:
    all_users.append(row.split("\n")[0])
f.close()

new_users = []
new_names = []
for i in range(len(all_users)):
    if all_users[i] not in new_users:
        new_users.append(all_users[i])
        #new_names.append(all_names[i])
f = open("users.csv","w+")
for i in range(len(new_users)):
    #row = all_users[i] + "," + all_names[i] + "\n"
    row = new_users[i]+"\n"
    f.write(row)
f.close()
