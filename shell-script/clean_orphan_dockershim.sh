#!/usr/bin/env bash

kill_orphaned_dockershim()
{
    shimpid=$1
    dockerid=$2
    childpid=$(ps --ppid $shimpid -o pid| grep -vi pid)
    if [[ -z $childpid ]];then
        echo "$shimpid has no child pid, kill it, and rm docker $dockerid"
        docker rm -f $dockerid || true
        kill -9 $shimpid
    fi
}


dockerd_pid=$(ps -C dockerd -o pid |grep -vi pid)
echo "dockerd_pid: $dockerd_pid"

docker_containerd_pid=$(ps --ppid $dockerd_pid -o pid|grep -vi pid)
if [[ -z $docker_containerd_pid ]];then
    docker_containerd_pid=$(ps -C containerd -o pid |grep -vi pid)
fi
echo "docker_containerd_pid : $docker_containerd_pid"

#dockershim_processes=$(ps --ppid $docker_containerd_pid -o pid,cmd |grep -vi pid )
ps --ppid $docker_containerd_pid -o pid,cmd |grep -vi pid  | while read shimprocess;
do
    dockerid=$(echo $shimprocess|grep -oE 'moby/[0-9a-z]+' |cut -d'/' -f2)
    shimpid=$(echo $shimprocess|awk '{print $1}')
    kill_orphaned_dockershim $shimpid $dockerid
done

# handler dockershim is child process of init process
ps --ppid 1 -o pid,cmd |grep containerd-shim | while read shimprocess;
do
    dockerid=$(echo $shimprocess|grep -oE 'moby/[0-9a-z]+' |cut -d'/' -f2)
    shimpid=$(echo $shimprocess|awk '{print $1}')
    kill_orphaned_dockershim $shimpid $dockerid
done

