#!/usr/local/env python
#coding=utf-8
#from tensorflow.python.grappler import item

class TreeNode(object):
    """tree node"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
class ListNode(object):
    '''List node'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self,item=None):
        self.stack = []
        if item:
            self.stack.append(item)
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is NULL!")
        return None
    def get_top(self):
        """return the top element"""
        if not self.is_empty():
            return self.stack[-1]
        print("Stack is Null!")
        return None
    def size(self):
        return len(self.stack)

class MyQueue(object):
    def __init__(self, item=None):
        self.queue = []
        if item:
            self.queue.append(item)
    def is_empty(self):
        return len(self.queue) == 0
    
    def push(self, item):
        self.queue.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Stack is NULL!")
        return None
    def get_head(self):
        """return the top element"""
        if not self.is_empty():
            return self.queue[0]
        print("Stack is Null!")
        return None
    def size(self):
        return len(self.queue)  

if __name__ == "__main__":
    queue = MyQueue()
    stack = Stack()
    for i in range(10):
        queue.push(i)
        stack.push(i)
    while not queue.is_empty():
        print(queue.pop(), stack.pop())
