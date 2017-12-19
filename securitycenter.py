#!/usr/bin/python
# Update Security Center with stuff from Amazon

import sys
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Custom modules
import update_scanzone
import update_repository
import update_assetlist


def update_data(sc_config, sc_repo_id, sc_scanzone_id, assetlist_id, ip_list):
    """Update our various data sources with a list of IPs"""
    # Admin users can only update scan zones and repositories
    security_token = get_token(sc_config, admintoken=True)
    update_scanzone.update_scanzone(security_token, sc_config, sc_scanzone_id, ip_list)
    update_repository.update_repository(security_token, sc_config, sc_repo_id, ip_list)
    # Admin users cant update asset lists
    security_token = get_token(sc_config, admintoken=False)
    update_assetlist.update_asset_list(security_token, sc_config, assetlist_id, ip_list)


def get_token(sc_config, admintoken):
    """HELP"""
    url = "https://" + sc_config['server'] + "/rest/token"
    if admintoken is True:
        payload = {'username': sc_config['admin_username'], 'password': sc_config['admin_password']}
    elif admintoken is False:
        payload = {'username': sc_config['org_username'], 'password': sc_config['org_password']}
    try:
        req = requests.post(url, data=json.dumps(payload), verify=False)
    except Exception as err:
        print "FAIL"
        sys.exit("[ERROR] Unable to connect to Security Center")

    if req.status_code == 200:
        respdata = json.loads(req.text)
        cookie_data = req.cookies['TNS_SESSIONID']
        token = respdata['response']['token']
    else:
        print req.status_code
        sys.exit("[ERROR] Not a 200")

    return token, cookie_data
