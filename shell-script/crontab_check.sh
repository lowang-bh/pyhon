#!/usr/bin/env bash
#########################################################################
# File Name: crontab_check.sh
# Author: longhui
# Created Time: 2018-08-27 11:47:58
#########################################################################

pgrep squid-monitor &>/dev/null || (cd /opt/squid/; nohup /opt/squid/squid-monitor > /dev/null 2>> error.log &)
