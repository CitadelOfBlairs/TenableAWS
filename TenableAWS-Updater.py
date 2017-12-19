#!/usr/bin/python
# Master script to get a list of Elastic IP addresses of active EC2 instances
# in our defined active regions


import argparse
import os
import sys

# My AWS modules
import configuration
import enumeration
import slack


def __main__():
    """Get this party started"""
    parser = argparse.ArgumentParser(description='AWS/Tenable Update Script of Doom')
    parser.add_argument('--configuration-file', '-c', dest='configfile', default='configuration.json', help='Configuration file to use')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.1')
    args = parser.parse_args()
    config = args.configfile

    print "\nAWS/Tenable Update Script of Doom"
    if not args.configfile:
        sys.exit(parser.print_help())
    else:
        # Configuration file
        slack_config = configuration.parse_configuration(config, required="slack")
        slack.notifyadmin(message="Updating AWS / Tenable data...")
        credentials = configuration.parse_configuration(config, required="aws_accounts")
        regions = configuration.parse_configuration(config, required="active_regions")
        sc_config = configuration.parse_configuration(config, required="sc_config")
        account_check = enumeration.account_check(credentials, regions, sc_config)


if __name__ == '__main__':
    __main__()
