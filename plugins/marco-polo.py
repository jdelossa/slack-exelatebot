import time
import requests
import shutil
import re
#import catch
crontable = []
outputs = []
from slackclient import SlackClient

def process_message(data):
        token = "xoxb-43078106134-1CvJViGymfBRYF0r5q1I5GYc"    # My Slack Token
        sc = SlackClient(token)

        Marco = ['marco', 'Marco']

        for i in Marco:

                if i in data['text']:
                        sendstring = "polo"
                        outputs.append([data['channel'], sendstring])
                break

        #catch_all(data)