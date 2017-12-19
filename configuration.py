#!/usr/bin/python
# Parse our configuration file for accounts and active regions

import json
import sys

slack_channel = ""
slack_token = ""


def parse_configuration(config, required):
    """Pull information from our JSON config file"""
    try:
        with open(config, 'r') as fh:
            jsondata = json.load(fh)
    except Exception as err:
        print err
        sys.exit("[ERROR] Unable to open config file")

    if required == "aws_accounts":
        return jsondata['aws_accounts']
    elif required == "active_regions":
        return jsondata['active_regions']
    elif required == "sc_config":
        return jsondata['sc_config']
    elif required == "slack":
        return jsondata['slack']
    else:
        sys.exit("[ERROR] Something has gone horribly wrong.")


def set_global_variables():
    """Set some globals so we can get them in other modules"""
    # TODO: Find a better way to do this ?
    global slack_channel
    global slack_token
    slack_config = parse_configuration(config='configuration.json', required='slack')
    slack_channel = slack_config['slack_channel']
    slack_token = slack_config['slack_token']
