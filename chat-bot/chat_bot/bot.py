import os
import json

import requests


class WhatABotChatBot:

    base_url = lambda self, token: f"https://api.telegram.org/bot{token}"

    def __init__(self, token):
        self.token = token

    @classmethod
    def build(cls, token=None):
        if not token:
            return cls(os.getenv(token))
        
        return cls(token)

    def get_updates(self, offset=None):
        url = self.base_url(self.token) 
        url = url + "/getUpdates?timeout=100"
        if offset:
            url = url + f"&offset={offset + 1}"

        response = requests.get(url)

        return json.loads(response.content)

    def send_message(self, msg, chat_id):
        url = self.base_url(self.token) 
        url = url + f"/sendMessage?chat_id={chat_id}&text={msg}"

        if msg is not None:
            requests.get(url)