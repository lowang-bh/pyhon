#!/usr/bin/env python

class stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def push(self, item):
        return self.stack.append(item)

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        if self.stack:
            return False
        return True


input = [6,5,4,3,2,1,7]
output = [-1]*len(input)
index = []
ss = stack()

for k, v in enumerate(input):
    top = ss.top()
    print(top)
    if ss.is_empty() or v <= ss.top():
        ss.push(v)
        index.append(k)
        print(ss.stack)
        continue

    while (not ss.is_empty() and ss.top() < v):
        ss.pop()
        ix = index.pop()
        output[ix]= v
        print(ss.stack, output)
    ss.push(v)
    index.append(k)
    
# for item in index:
#     output.insert(item, -1)
print(output, index)
