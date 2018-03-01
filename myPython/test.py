#!/usr/bin/env python
# coding=UTF-8
import re

print "python 中文测试"
text = "Goo is a handsome boy, he is cool, clever, and so on..."
patten=r"\shandsome\s"
m = re.match(patten,text)
if m:
	print m.group(0)
else:
	print "not match"
	
m = re.search(patten,text)
if m:
	print m.group(0),m.groups()
else:
	print "not search"

res = None
if not res:
    print "res is  None"
else:
    print "res is not None"

group_inter =3
index = 0

neInfo={"a":"1", "b":"2"}
nelenth=len(neInfo)
print nelenth
for ne in neInfo:
	print ne, neInfo[ne]
	index +=1
	nelenth -=1
	print "add_task" , (index, nelenth)
	if index >=3 or nelenth == 0:
		print "start process"
		index = 0

		
import random
def func(ok):
	if ok:
		a = random.random()
	else:
		# import random
		a = random.randint(1, 10)
	return a
print func(False)
print func(True)
def set_axis(x,y,xlabel="x",ylabel="y", *args,**kwargs):
	print x, y, xlabel, ylabel, args, kwargs

set_axis(2, 3, "test1", "test2")

def myenumerate(sequence):
	n = -1
	slen = len(sequence)
	for elem in reversed(sequence):
		yield n + slen, elem
		n = n - 1
l = ['a', 'b', 'c', 'd', 'e']
for k, v in myenumerate(l):
	print "index=%s,value=%s" % (k, v)
class X(object):pass
class Y(X):pass
class Z(object):pass



class A(Y,Z):
	def test(self):
		print "test in A"
class B(A):
	pass
class C(A):
	def test(self):
		print "test in C"
class D(B, C):
	def test(self):
		super(D, self).test()
class Bb(B):pass
class E(Bb, C):
	def test(self):
		super(E, self).test()
e = E()
e.test()
print E.__mro__
d = D()
print D.__mro__
d.test()
class T(object):
	x = 100
	def __new__(cls, *args, **kwargs):
		print args, kwargs
		obj = object.__new__(cls, *args, **kwargs)
		print id(obj)
		return obj
	def __init__(self, *args, **kwargs):
		print args, kwargs
		# return 1, no non-None value shoud be return
	@classmethod
	def info(cls):
		print cls
	def __get__(self, ins, cls):
		print self, ins, cls

t1 = T(100, 90)
T.info()
t2 = T(10, 2)
t2.info()
print t2.x

