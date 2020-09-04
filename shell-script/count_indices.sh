#!/usr/bin/env bash
#########################################################################
# File Name: count_indices.sh
# Author: longhui
# Created Time: 2019-07-03 18:15:04
#########################################################################

curl -XGET -s -u sa:1q2w3e4r   'http://es.example.com/_cat/indices?v' | tail -n +2 > indices1.txt

cat indices1.txt |awk  -F "_2019" '{ print $1}' | sort |uniq -c

