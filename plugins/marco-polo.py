import time
import requests
import shutil
import re
crontable = []
outputs = []
from slackclient import SlackClient

def process_message(data):
        token = "xoxo"    # Your Slack Token
        sc = SlackClient(token)
        print sc.api_call("users.info",user=data['user'])
        print sc.api_call("channels.info",channel=data['channel'])

        Greetings = ['Hi', 'Hello', 'hi', 'hello', 'HI', 'HELLO']
        marco = ['Marco']
        polo = ['Polo']

        # Say Hello
        for greeting in Greetings:

                if greeting in data['text']:
                        sendstring = "Say Marco"
                        outputs.append([data['channel'], sendstring])
        # Say marco
        for m in marco:

                if m in data['text'] or m.lower() in data['text'] or m.upper() in data['text']:
                        sendstring = "Polo!\nSay it again"
                        outputs.append([data['channel'], sendstring])

        # Say polo
        for p in polo:

                if p in data['text'] or p.lower() in data['text'] or p.upper() in data['text']:
                        sendstring = "Marco!\nBut next time say Marco"
                        outputs.append([data['channel'], sendstring])
                break
