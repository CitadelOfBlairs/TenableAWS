#!/usr/bin/python
# Update Tenable scan zones with data given to us

import sys
import requests
import json
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_asset_list(ip_list):
    """Create a dict of our assets for upload"""
    asset_string = ",".join(ip_list)
    ipdict = dict()
    ipdict['ipList'] = asset_string

    return ipdict


def update_scanzone(security_token, sc_config, sc_scanzone_id, ip_list):
    """Update our scan zone with new IPs"""
    headers = {'X-SecurityCenter': str(security_token[0]), 'Content-Type': 'application/json'}
    cookie = {'TNS_SESSIONID': security_token[1]}
    asset_dict = get_asset_list(ip_list)
    URL = "https://" + sc_config['server'] + "/rest/zone/" + sc_scanzone_id
    print "[UPDATE] Scan zone...",
    req = requests.patch(URL, cookies=cookie, headers=headers, verify=False, json=asset_dict)
    status = req.status_code
    if status == 200:
        print " OK"
    else:
        sys.exit("\n[ERROR] We got an error code back: %s " % status)
