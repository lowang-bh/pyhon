#!/usr/bin/env bash
#########################################################################
# File Name: clean_unused_vhd.sh
# Author: longhui
# Created Time:
# Description: clean unused disk in xenserver
#########################################################################

usedvbds=$(xe vbd-list |grep vdi-uuid |grep -v "not in database" | awk -F': ' '{print $2}')
cd /var/run/sr-mount/aa6f62a6-49c1-8fa4-8ae9-9b5e7f19dd19
for f in  *.vhd;
do
    used=0
    for vbd in $usedvbds;
    do
        if [[ ${vbd}.vhd == ${f} ]];then
            echo `ls -lh $f`, is used
            used=1
        fi
    done
    if [[ $used -eq 0 ]];then
        echo `ls -lh $f`, is not used
    fi
done
