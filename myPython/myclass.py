#!/usr/bin/env python
"This is a test module"

import os
import sys

debug=True

class testClass():
    "Test Class"
    print "print this infor in class:call in testClass"

def test():
    "test function"
    var=testClass()
    if debug:
        print "run test() function"

if __name__ == "__main__":
    test()