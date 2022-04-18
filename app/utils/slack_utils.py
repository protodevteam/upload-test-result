import sys
import os
import requests
import json

def send_message(self, text_message, image_url):
    slack_incoming_url = self.slack_incoming_url
    slack_payload = {
        "attachments": [
            {
                "text": text_message,
                "color": "#764FA5"
            }
        ]
    }

    # Send to slack
    req = requests.post(url=slack_incoming_url, data=json.dumps(slack_payload))
    print(req)