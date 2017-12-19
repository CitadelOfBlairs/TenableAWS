Tenable AWS
===========

Scenario:
---------

You're an AWS house using Tenable Security Center with Nessus to do scanning of stuff.
Elastic IP addresses do change every now and again and maintaining the Tenable asset lists,
scan zones and repository data is a huge waste of time.

This script will pull Elastic IP addresses from your EC2 infrastructure and update
the data repositories in Security Center. It is meant to be run from a Linux box via cron.

It does require initial setup of the scan zones, asset lists and repositories for the
configuration file bits.


Requirements
------------

 * [Boto3](https://github.com/boto/boto3)
 * [Python Requests](https://github.com/requests/requests)


Scripts
-------

 * TenableAWS-Updater.py - Master script
 * configuration.py - Get accounts and active regions
 * enumeration.py - EC2 Instance enumeration
 * securitycenter.py - Updates the various things in Security Center
 * configuration.json.dist - Example configuration file
 * update_assetlist.py - Updates the asset list in Security Center
 * update_repository.py - Updates the repository in Security Center
 * update_scanzone.py - Updates the scan zone in Security Center
 * slack.py - For Slack notifications


TODO:

 * Automate the creation of asset lists, scan zones and repositories.
