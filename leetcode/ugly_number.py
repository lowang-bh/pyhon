#!/usr/bin/env python
from lib.DataStructure import MyQueue
import Queue

def get_ugly_num(k):
    if k <= 0:
        return 0
    q2, q3, q5 = MyQueue(2), MyQueue(3), MyQueue(5)
    minus = 0
    for i in range(1, k + 1):
        v2, v3, v5 = q2.get_head(), q3.get_head(), q5.get_head()
        minus = min([v2, v3, v5])
        print(minus,)
        if minus == v2:
            q2.pop()
            q2.push(2 * minus)
            q3.push(3 * minus)
            q5.push(5 * minus)
        elif minus == v3:
            q3.pop()
            q3.push(3 * minus)
            q5.push(5 * minus)
        else:
            q5.pop()
            q5.push(5 * minus)

    return minus


get_ugly_num(100)

q = Queue.Queue()
