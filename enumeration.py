#!/usr/bin/python
# Run EC2 enumeration against chosen accounts


import os
import sys
import json
try:
    import boto3
except Exception as err:
    print "[ERROR] " + str(err)
# Custom modules
import securitycenter
import slack


def account_check(credentials, regions, sc_config):
    """Return our account list"""
    for account, v in credentials.iteritems():
        tmp_ip_list = []
        for k, v in regions.iteritems():
            region = v['region']
            sc_repo_id = v['sc_repo_id']
            sc_scanzone_id = v['sc_scanzone_id']
            assetlist_id = v['assetlist_id']
            region_ip_list = run_enumeration(credentials, account, region)
            print "[AUDIT] " + str(len(region_ip_list)) + " public servers in " + k
            message = str(len(region_ip_list)) + " servers in " + k
            slack.notifyadmin(message)
            tmp_ip_list.append(region_ip_list)
        # TODO: Figure out a better way to do this
        master_ip_list = []
        for item in tmp_ip_list:
            master_ip_list += item
        if len(master_ip_list) == 0:
            print "[UPDATE] None required"
        else:
            print "[UPDATE] Updating data repositories with " + str(len(master_ip_list)) + " new IP addresses."
            message = "Updating data repositories with " + str(len(master_ip_list)) + " new IP addresses."
            slack.notifyadmin(message)
            securitycenter.update_data(sc_config, sc_repo_id, sc_scanzone_id, assetlist_id, master_ip_list)

    print "\n[DONE] We are done here."


def run_enumeration(credentials, account, region):
    """Check whats running in EC2"""
    ip_list = []
    accesskey = credentials[account]['AccessKey']
    secretkey = credentials[account]['Secret']
    ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=accesskey, aws_secret_access_key=secretkey)
    instancedata = ec2.describe_instances()
    instance_meta = instancedata['Reservations']
    if len(instance_meta) > 0:
        for k, v in enumerate(instance_meta):
            try:
                ip_list.append(v['Instances'][0]['PublicIpAddress'])
            except Exception as err:
                pass
    else:
        pass

    return ip_list
