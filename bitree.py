#!/usr/bin/env python
class Node(object):
    def __init__(self,data=None,lchild=None,rchild=None):
        self.data=data
        self.lchild=lchild
        self.rchild=rchild

class Tree(object):
    def __init__(self):
        self.root=Node()
        self.myqueue = []
    def add(self, elem):
        node=Node(elem)
        if self.root.data is None:#if the tree is NULL,assign to root
            self.root = node
        else:
            tree_node=self.myqueue[0]
            if tree_node.lchild ==None:
                tree_node.lchild = node
            else:
                tree_node.rchild = node
                self.myqueue.pop(0)
        self.myqueue.append(node) 

def pre_order(tree):
    if tree==None:
        return
    print tree.data,
    pre_order(tree.lchild)
    pre_order(tree.rchild)

if __name__=="__main__":
    A=Node(1)
    B=Node(2)
    C=Node(3)
    D=Node(4)
    A.lchild=B
    A.rchild=C
    B.rchild=D
#   A
# B      C
#``    D
    pre_order(A)
    print "-----------------"
    tree=Tree()
    for elem in range(10):
        tree.add(elem)
    pre_order(tree.root)
    print "OK"
