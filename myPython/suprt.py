import collections
import logging

logging.basicConfig(level='INFO')

class LoggingDict(dict):
    # Simple example of extending a builtin class
    def __setitem__(self, key, value):
        logging.info('Setting %r to %r' % (key, value))
        super(LoggingDict, self).__setitem__(key, value)

class LoggingOD(LoggingDict, collections.OrderedDict):
    # Build new functionality by reordering the MRO
    pass

ld = LoggingDict([('red', 1), ('green', 2), ('blue', 3)])
print ld
ld['red'] = 10

ld = LoggingOD([('red', 1), ('green', 2), ('blue', 3)])
print ld
ld['red'] = 10
print ld
print '-' * 20

import sys
class csim_log(logging.Logger):
    def __init__(self, name):
        super(csim_log,self).__init__(name)
        print "csim_log init"

log=csim_log("csim log")
log.propagate = 0
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("%(message)s"))
log.addHandler(handler)
log.info("test ok")
log.__init__("init")

class B(object):
    def __new__(self, *args, **kwargs):
        print "In class B's __new__ fuction"
        # return object.__new__(self, *args, **kwargs)
    def __init__(self, args):
        print "in class B",
        print "args=", args
    def father(self, args):
        print "in B class.father", args
    def son(self, args):
        print "in B class.son", args
class C(B):
    def __new__(self, *args, **kwargs):
        print "in Class C's __new__ function"
        # B.__new__(self, *args, **kwargs)
        return object.__new__(self, *args, **kwargs)
    def __init__(self, args):
        super(C, self).__init__(args)
        print "in class C"
    def father(self, args):
        super(C,self).father(args)
        print "in C class.father", args
    def son(self, args):
        #super(C,self).son(args)
        print "in C class.son", args

b=B("b class")
c=C("c class") 
print B.__dict__
print C.__dict__   
# b.father("b father")
c.father("c father")
# b.son("b son")
c.son("c son")
