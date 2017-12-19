#!/usr/bin/python
# Send notifications via Slack

try:
    from slackclient import SlackClient
except Exception as err:
    sys.exit("[ERROR] Unable to import Slack module")
import sys
# Custom modules
import configuration
configuration.set_global_variables()


def notifyadmin(message):
    """"Send a notification that keys have been disabled"""
    sc = SlackClient(configuration.slack_token)
    sc.api_call("chat.postMessage", channel=configuration.slack_channel, as_user=True, text=message)
