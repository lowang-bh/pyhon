#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):
    name = "person_class"
    total = 0
    number = 0
    
    def __init__(self):
        self.total += 1
        Person.number +=1

p1= Person()
p2 = Person()
p1.name = "p1"

print(p1.name, p2.name, Person.name)
print(p1.total, p1.number)
print(p2.total,p2.number)
print(Person.total, Person.number)
print(dir(p1))
print(dir(p2))
