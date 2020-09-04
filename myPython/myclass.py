#!/usr/bin/env python
"This is a test module"

debug=True

class testClass(object):
    "Test Class"
    print "print this infor in class:call in testClass"
    
    def funcParent(self):
        print("funcParent")
        self.funcChild() # when instance is subClass, it will call subClass's funcChild

    def funcChild(self):
        print("funcChild in class Parent")


class subClass(testClass):
    
    def funcChild(self):
        #super(subClass, self).funcChild()
        print("funcChild in class subClass")



def test():
    "test function"
    var=testClass()
    if debug:
        print "run test() function"
    sub = subClass()
    sub.funcParent()
    print("-------")
    sub.funcChild()

if __name__ == "__main__":
    test()
