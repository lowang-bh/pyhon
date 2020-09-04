#!/usr/bin/env bash
#########################################################################
# File Name: clean_unused_vhd.sh
# Author: longhui
# Created Time: 
# Description: clean unused disk in xenserver
#########################################################################

# 实际磁盘文件uuid
vdiuuids=$(xe vdi-list params=uuid managed=true|awk -F': ' '{print $2}')
for vdiuuid in ${vdiuuids};
do
    # xe vdi-list uuid=${vdiuuid} params=vbd-uuids  查找vdi挂载在哪个vm下的vbd
    vbds=$(xe vdi-list uuid=${vdiuuid} params=vbd-uuids |awk -F': ' '{print $2}')
    if [[ -z $vbds ]];then
        vdisize=$(xe vdi-list uuid=${vdiuuid} |grep virtual-size |awk -F': ' '{print $2}')
        size=$(($vdisize/1024/1024))
        echo "vdiuuid=$vdiuuid has no vbd, so no vm use it, size is ${size}M"
        continue
    fi
        
    for vbduuid in ${vbds//;/};
    do
        vmnamelabel=$(xe vbd-list uuid=$vbduuid params=vm-name-label |awk -F': ' '{print $2}')
        if [[ -z  $vmnamelabel ]];then
            echo "vbd_uuid=$vbduuid," has no vm
        else
            echo "namelabel=$vmnamelabel", vdiuuid=$vdiuuid, vbd_uuid=$vbduuid
        fi
    done
done


# 查找sr下面的vdi
#SRUUID=aa6f62a6-49c1-8fa4-8ae9-9b5e7f19dd19
#vdiuuids=$(xe vdi-list params=uuid sr-uuid=${SRUUID} |awk -F': ' '{print $2}')
#cd /var/run/sr-mount/aa6f62a6-49c1-8fa4-8ae9-9b5e7f19dd19
#for vhd in *.vhd;
#do
#    findvdi=0
#    for vdiuuid in $vdiuuids;
#    do
#        if [[ ${vhd} == ${vdiuuid}.vhd ]];then
#            echo "$vhd found its vdi uuid"
#            findvdi=1
#            break
#        fi
#    done
#    if [[ $findvdi -eq 0 ]];then
#        echo "$vhd has no vdi uuid"
#    fi
#done
