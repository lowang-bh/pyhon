#!/usr/bin/env python
import mock
import unittest
import sys
from scripts.test2 import another

'''
class myclass:
    def __init__(self):
        print "init"
    def get_name(self,name):
        print "in get_name"
        return name
    
def another(name):
    t=myclass()
    ret = t.get_name(name)
    print ret
'''
class mockclass():
    def __call__(self):
        return self
    def __init__(self):
        print "mock init"
        self.element="init mockclass"
    def get_name(self,name):
        print "in mock get_name"
        return name
    def call_function(self,classname):
        classname.get_name(self.element)

def new_call(mockclass):
    print "I am in mock call"
    print mockclass
def mock_function_of_class(name):
    print "I am in a mock function of class"
    return name

class test_another(unittest.TestCase):
    def setUp(self):
        self.patch_myclass=mock.patch('scripts.test2.myclass',new_callable=mockclass)
        self.mockclass=self.patch_myclass.start()
    def tearDown(self):
        self.patch_myclass.stop()
    
    @mock.patch('scripts.test2.myclass.get_name')
    @mock.patch('scripts.test2.call_class_test')
    def test_another(self,mock_call,mock_class_method):
        name="mock"
        self.mockclass.return_value = mockclass()
        mock_call.side_effect=new_call
        mock_class_method.side_effect=mock_function_of_class
        another(name)
        mock_call.assert_called_once_with(self.mockclass)

if __name__ == "__main__":
    unittest.main()