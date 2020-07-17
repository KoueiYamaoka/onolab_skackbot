# -*- coding: utf-8 -*-
from slack import WebClient
import slackbot_setting as ss


class Slackbot:
    """
    Slack bot using slack.WebClient()

    attributes
    ----------
    client: slack.WebClient(your API token)
        your slack web client
    user_dict: dict
        pair of user name and id
    """

    def __init__(self):
        self.client = WebClient(ss.token)
        self.user_dict = self.get_user_dict()

    def get_user_dict(self):
        """
        Get the pair of user name and id

        return
        ----------
        user_dict: dict
            Pair of user name and id
        """

        response = self.client.users_list()
        user_dict = {}
        for user in response.data["members"]:
            if user["profile"]["display_name"] == "":
                user_dict[user["profile"]["real_name"]] = user["id"]
            else:
                user_dict[user["profile"]["display_name"]] = user["id"]

        return user_dict

    def send_direct_message(self, username, message):
        """
        Send a direct message

        parameters
        ----------
        username: str
            User name (real_name or display_name)
        message: str
            Message to be posted
        """

        uid = self.user_dict[username]
        self.client.chat_postMessage(channel=uid, text=message)
