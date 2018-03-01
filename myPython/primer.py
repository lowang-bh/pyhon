#!/usr/bin/env python
from DataStructure import MyQueue
def get_ugly_num(k):
    if k <= 0:
        return 0
    q3,q5,q7=MyQueue(3),MyQueue(5),MyQueue(7)
    minus=0
    for i in range(1,k+1):
        v3,v5,v7=q3.get_head(),q5.get_head(),q7.get_head()
        minus = min([v3,v5,v7])
        if minus == v3:
            q3.pop()
            q3.push(3*minus)
            q5.push(5*minus)
            q7.push(7*minus)
        elif minus == v5:
            q5.pop()
            q5.push(5*minus)
            q7.push(7*minus)
        else:
            q7.pop()
            q7.push(7*minus)
        
    return minus

for i in range(1,15):
    print(i, get_ugly_num(i))        
        