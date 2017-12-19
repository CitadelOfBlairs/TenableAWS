#!/usr/bin/python
# Update Tenable asset lists (initial list must be created)

import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import os
# Ignore Insecure TLS warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_asset_list(ip_list):
    """Get our list of new assets from file"""
    asset_string = ",".join(ip_list)
    ipdict = dict()
    ipdict['definedIPs'] = asset_string

    return ipdict


def update_asset_list(security_token, sc_config, assetlist_id, ip_list):
    """Update the asset list in Security Center from given IPs"""
    org_user = sc_config['org_username']
    org_password = sc_config['org_password']
    headers = {'X-SecurityCenter': str(security_token[0]), 'Content-Type': 'application/json'}
    cookie = {'TNS_SESSIONID': security_token[1]}
    URL = "https://" + sc_config['server'] + "/rest/asset/" + assetlist_id
    asset_dict = get_asset_list(ip_list)
    print "[UPDATE] Asset list...",
    req = requests.patch(URL, cookies=cookie, headers=headers, verify=False, json=asset_dict)
    if req.status_code == 200:
        print " OK"
    else:
        print "[ERROR] Something has gone horribly wrong: " + str(req.status_code)
        print req.text
