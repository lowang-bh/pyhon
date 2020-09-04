#!/usr/bin/env bash


vmnames=$(xe vm-list params=name-label |cut -d':' -f 2 |grep -oE xs10[-_0-9a-zA-Z.]+)


qemuprocess=$(for pid in $(pgrep -f qemu); do ps -p $pid -o cmd=;done)

for vmname in $vmnames;
do
    vifuuid=$(xe vif-list vm-name-label=$vmname params=uuid |cut -d':' -f 2 |grep -oE [-0-9a-zA-Z.]+)
    mac=$(xe vif-param-list uuid=$vifuuid| grep "MAC ( RO):" | awk {'print $4'})

    echo $qemuprocess | grep -q $mac
    if [[ $? -eq 0 ]];then
        echo "$vmname, $mac, process exist"
    else
        echo "$vmname, $mac, process not found"
    fi

done
