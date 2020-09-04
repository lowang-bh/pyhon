#!/usr/bin/env bash

namespaces=$(kubectl get ns |tail -n +2 |awk '{print $1}')


for ns in $namespaces;do
    # echo $ns
    apps=$(kubectl get runtimeapps.console.lain.io -n $ns |tail -n +2 |awk '{print $1}')
    for app in $apps;do
        #output=$(kubectl get runtimeapps.console.lain.io  $app -n $ns -o yaml|  grep -E "limits|replicas" -A 2)
        cpu=$(kubectl get runtimeapps.console.lain.io  $app -n $ns -o yaml|  grep " limits" -A 2 |grep cpu |awk '{print $2}')
        mem=$(kubectl get runtimeapps.console.lain.io  $app -n $ns -o yaml|  grep " limits" -A 2 |grep memory |awk '{print $2}')
        rep=$(kubectl get runtimeapps.console.lain.io  $app -n $ns -o yaml|  grep " replicas" -A 2 |grep replicas|head -n 1 |awk '{print $2}')
        printf "%-10s %10s %10s %10s %10s" $ns  $app $rep $cpu $mem     
    done
done
