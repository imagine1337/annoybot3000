import requests
import json
import time
from datetime import datetime
token = "discord token here"
id = "victim id here"
channel = "target channel id here"

def sendmsg(txt,channel):
    c = requests.post(f'https://discord.com/api/v9/channels/{channel}/messages',headers={'authorization':token}, data={'content': txt,'content-type':'application/json'})
def getmsgs(channel):
    c = requests.get(f'https://discord.com/api/v8/channels/{channel}/messages?limit=10',headers={'authorization':token})
    return c.json()

msgarr=[]
while 1:
    time.sleep(5)
    f = getmsgs(channel)
    l=0
    for x in f:
        if x['author']['id']==id and x['id'] not in msgarr:
            msgarr.append(x['id'])
            l+=1
    if l>1:
        print(f'{l} blocked messages')
        sendmsg(f'{l} blocked messages',channel)
    elif l==1:
        print(f'{l} blocked message')
        sendmsg(f'{l} blocked message',channel)
