#!/usr/bin/env bash
dir=$1

if [[ -z $dir ]];then
	exit 1
else
	if [[ $dir == /user/lain/logsys/logs/*/* ]] && [[ $dir != /user/lain/logsys/logs/prod ]];then
	echo $dir
	#hdfs dfs -rm -r $dir
	fi
fi
