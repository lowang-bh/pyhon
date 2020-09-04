#!/usr/bin/env python

etcd_ignore=[]
etcd_tmp=[]
with open("/Users/wang/Documents/etcd.txt") as fi:
    for line in  fi:
        split_line = str(line).rstrip().split(",")
        if len(split_line) == 2:
            etcd_ignore.append(split_line[0]), etcd_tmp.append(split_line[1])
        else:
            print split_line
            
            
            
for item in etcd_ignore:
    if item not in etcd_tmp:
        print item


print "don't rm"
for item in etcd_tmp:
    if item not in etcd_ignore:
        print item
