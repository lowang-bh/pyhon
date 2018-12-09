#!/usr/bin/env bash
#########################################################################
# File Name: service.sh
# Author: longhui
# Created Time: 2018-06-11 17:40:10
#########################################################################

#JAVA_HOME=/usr/java/default
#export JAVA_HOME
KAFKA_HOME={{ kafka.install_dir }}/{{ kafka_name }}/
KAFKA_USER=kafka
SHUTDOWN_WAIT=20

NAME="$(basename $0)"
unset ISBOOT
if [ "${NAME:0:1}" = "S" -o "${NAME:0:1}" = "K" ]; then
    NAME="${NAME:3}"
    ISBOOT="1"
fi

# Get instance specific config file
if [ -r "/etc/sysconfig/${NAME}" ]; then
    . /etc/sysconfig/${NAME}
fi

kafka_pid() {
echo `ps aux | grep ".jar kafka.Kafka ./config/server.properties"  | grep -v grep | awk '{ print $2 }'`
}

start() {
	pid=$(kafka_pid)
	if [ -n "$pid" ]; then
		echo "Kafka is already running (pid: $pid)"
	else
		echo -n "Starting kafka: "
  		#ulimit -n 65536
  		#ulimit -s 10240
  		#ulimit -c unlimited
		cd $KAFKA_HOME
		su ${KAFKA_USER} -c "env JMX_PORT={{ kafka.jmx_port }} ./bin/kafka-server-start.sh ./config/server.properties" >> /var/log/kafka.log 2>&1 &
		echo "done."
	fi
	return 0;
}
stop() {
	pid=$(kafka_pid)
	if [ -n "$pid" ]; then
		echo -n "Shutting down kafka: "
		cd $KAFKA_HOME
		kill $pid
		#${STOP_KAFKA}
		let kwait=$SHUTDOWN_WAIT
		count=0;
		until [ `ps -p $pid | grep -c $pid` = '0' ] || [ $count -gt $kwait ]; do
			echo -n -e "\nwaiting for processes to exit";
			sleep 1
			let count=$count+1;
		done
		if [ $count -gt $kwait ]; then
			echo -e "\nkilling processes which didn't stop after $SHUTDOWN_WAIT seconds"
			kill -9 $pid
			sleep 1
		else
			echo " Done"
		fi
	else
		echo "Kafka is not running"
	fi

	return 0
}
abort() {
	pid=$(kafka_pid)
	if [ -n "$pid" ]; then
		echo -n "Shutting down kafka: "
		cd $KAFKA_HOME
		kill $pid
		let kwait=1
		count=0;
		until [ `ps -p $pid | grep -c $pid` = '0' ] || [ $count -ge $kwait ]; do
			echo -n -e "\nwaiting for processes to exit";
			sleep 1
			let count=$count+1;
		done
		if [ $count -ge $kwait ]; then
			echo -e "\nkilling processes which didn't stop after $kwait seconds"
			kill -9 $pid
			sleep 1
		else
			echo " Done"
		fi
	else
		echo "Kafka is not running"
	fi

	return 0
}
case "$1" in
	start)
		start
		;;
	stop)
		stop
		;;
	abort)
		abort
		;;
	restart)
		stop
		start
		;;
	status)
		pid=$(kafka_pid)
		if [ -n "$pid" ]; then
			echo "Kafka is running with pid: $pid"
		else
			echo "Kafka is not running"
		fi
		;;
	*)
		echo "Usage: $0 {start|stop|restart|status|abort}"
esac
exit 0

