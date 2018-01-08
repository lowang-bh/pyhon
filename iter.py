#!/usr/bin/env python
class Container:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __iter__(self):
        print "[LOG] I made this iterator!"
        return self
    def next(self):
        print "[LOG] Calling __next__ method!"
        if self.start < self.end:
            i = self.start
            self.start +=1
            return i
        else:
            raise StopIteration()

c = Container(1,7)
for i in c:
    print i
