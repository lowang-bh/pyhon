#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import urllib2
import os
import sys

sys.path.append('D:\myPython')
print os.getcwd()
'''
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u=urllib2.urlopen(url)
localfile = open('iris.csv','w')
localfile.write(u.read())
localfile.close()
'''
from numpy import genfromtxt,zeros
filepath = 'D:\\myPython\\iris.csv'

data = genfromtxt('iris.csv', delimiter=',',usecols=(0,1,2,3))
target = genfromtxt('iris.csv', delimiter=',',usecols=(4),dtype=str)

print data.shape,target.shape
print set(target)
print data[target=='setosa',0]
from pylab import plot,show
plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
plot(data[target=='virginica',0],data[target=='virginica',2],'go')
show()
print target=='setosa'
