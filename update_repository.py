#!/usr/bin/python
# Update Tenable repositories (initial repository must exist)

import requests
import json
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_repo_list(ip_list):
    """Get a list of IPs to add to our repo from file"""
    repo_string = ",".join(ip_list)
    ipdict = dict()
    ipdict['ipRange'] = repo_string

    return ipdict


def update_repository(security_token, sc_config, sc_repo_id, ip_list):
    """Get a list of repositories in our Security Center"""
    repo_dict = get_repo_list(ip_list)
    headers = {'X-SecurityCenter': str(security_token[0]), 'Content-Type': 'application/json'}
    cookie = {'TNS_SESSIONID': security_token[1]}
    URL = "https://" + sc_config['server'] + "/rest/repository/" + sc_repo_id
    print "[UPDATE] Repository...",
    req = requests.patch(URL, cookies=cookie, headers=headers, verify=False, json=repo_dict)
    if req.status_code == 200:
        print " OK"
    else:
        print "[ERROR] Something has gone horribly wrong: " + str(req.status_code)
