# -*- coding: utf-8 -*-
import argparse
from Slackbot import Slackbot


def parse_cmd_args():
    parser = argparse.ArgumentParser(
        description="Send a notification to your slack when a script finishes."
    )
    parser.add_argument(
        "username",
        type=str,
        help="Username to send a direct message (display_name or real_name)",
    )
    parser.add_argument(
        "-n",
        "--script_name",
        type=str,
        default="Your script",
        help="Running script name",
    )
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_cmd_args()
    user = args.username
    message = args.script_name + " is completed :tada:"

    bot = Slackbot()
    bot.send_direct_message(user, message)
