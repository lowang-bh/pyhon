#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3, time, os, sys, atexit, threading
from optparse import OptionParser

try:
    from Utils.log import log as logging
    logging.info("from Utils.log import log ok")
except ImportError:
    try:
        from lib.Log.log import log as logging
        logging.info("from lib.Log.log import log ok")
    except ImportError:
        import logging
        # logging.basicConfig(level='INFO')
        log = logging.Logger('root')
        # getLogger will get the default root logger as its parent, which is different from logging.Logger

        # log = logging.getLogger("test")
        # log.setLevel(logging.DEBUG)
        #log = logging.Logger('test')
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter("%(asctime)s,%(lineno)4d : %(message)s","%d/%b/%Y:%H:%M:%S %z"))
        log.addHandler(handler)
        logging = log
logging.info("OK")

class Card(object):
    """
    a base class
    """

    def __init__(self):
        super(Card, self).__init__()

        # generated properties: card_name XCM 1-A-6A
        self._card_name = None
    def get_chip_dbi_shelf_slot(self):
        '''
        get dbi slot in chipsim
        '''
        logging.info("In Card: get_chip_dbi_shelf_slot ")
    def dbi_plug_unplug(self, *args, **kwargs):
        logging.info("In Card: dbi_plug_unplug ")
        print args, kwargs
        a = kwargs['a']
        b = kwargs['b']
        logging.info("a=%s,b=%s", a, b)
        self.get_chip_dbi_shelf_slot()
        # raise NotImplementedError("Derived class should implement.")
    def do_final_check(self):
        logging.info("do_final_check: in Card Class")

class XsmCard(Card):
    def __init__(self):
        super(XsmCard, self).__init__()

    def get_chip_dbi_shelf_slot(self):
        '''
        get dbi slot in chipsim
        '''
        logging.info( "In XSMcard: get_chip_dbi_shelf_slot")
    def do_final_check(self):
        logging.info("do_final_check: in XsmCard Class")

class LineCard(Card):
    def __init__(self):
        super(LineCard, self).__init__()

    def do_final_check(self):
        logging.info("do_final_check: in LineCard Class")

class PtimCard(XsmCard, LineCard):
    def __init__(self):
        super(PtimCard, self).__init__()
    def do_final_check(self):
        # XsmCard.do_final_check(self)
        super(PtimCard, self).do_final_check() #  search Xsmcard first, then LineCARD
        logging.info("do_final_check: in PtimCard Class")

def test_global_variable(root):
    log.info("The variable define in main, is global for func to get: root=%s" % tree)

def test_default_param(n, l=[], d={}):
    l.append(n)
    d[n] = n
    log.info( l, d)
    return l

class _Singleton(object):
    def __init__(self, name=None):
        self.name = name
        print "name=%s" % name

    def __str__(self):
        return  str(self.name)

class HvAccess(object):
    """
    function doc
    """

    ssh_instance_refcount = 0
    instance_lock = threading.Lock()
    lock = threading.RLock()
    # pylint: disable=redefined-outer-name
    def __new__(cls, *args, **kwds):
        '''
        Implement the Singleton pattern
        '''
        logging.info("In self.__new__ function")
        instance = cls.__dict__.get("__it__")
        if instance is not None:
            log.info("Already has instance, get it and return...")
            return instance

        # need to double check the instance. it's double check
        with cls.instance_lock:

            instance = cls.__dict__.get("__it__")
            if instance is not None:
                return instance
            cls.__it__ = instance = object.__new__(cls)

            log.info("create new instance for hv_access and return")

        return instance

    def del_instance(self):
        #self.__del__()
        self.__del__()
        self.__class__.__it__ = None

    def __init__(self, hostname=None, user="root", passwd="infinera", logfile=None):
        # log.debug("Try to get init lock...")
        logging.info("in hv accecss init")
        with self.instance_lock:
            # log.debug("Get init lock")
            self.__class__.ssh_instance_refcount += 1


# test Single Class
class Singleton(type):
    def __init__(cls, name, base, dic):
        log.info("In Singleton init: %s, base=%s, %s", name, base, dic)
        super(Singleton, cls).__init__(name, base, dic)
        cls.instance = None
    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
            log.info("create new instance: %s", id(cls.instance))
        else:
            log.info("Instance already exist: %s", id(cls.instance))
        return cls.instance

class mySingleton(object):
    __metaclass__ =  Singleton
    pass

# if the class's meta 's call is override
class anotherSignle(object):
    __metaclass__ =  Singleton

    def __call__(self, *args, **kwargs):
        log.info("override call:")
        pass

class Person(mySingleton):
    def __init__(self, name=None, age=None):
        super(Person, self).__init__()
        self.name = name
        self.age = age

    def __getattr__(self, item):
        log.info("In getattr: %s" %item)
        log.info("If property or __getattribute__ raise AttributeError, __getattr__ WILL called")

    @property
    def att(self):
        log.info("In property")
        if 'x' in self.__dict__:
            return self.x
        else:
            raise AttributeError


class testPerson(anotherSignle):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


class Container:
    def __init__(self, start=0, end=0):
          self.start = start
          self.end = end

    def __iter__(self):
          print "[LOG] I made this iterator!"
          return self

    def next(self): # python2.7中为next，python3中为__next__
        print "[LOG] Calling __next__ method!"
        if self.start < self.end:
            i = self.start
            self.start +=1
            return i
        else:
              raise StopIteration()

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item
class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)

class Privacy:
    def __setattr__(self, key, value):
        if key in self.privates:
            raise Exception("private attr")
        else:
            self.__dict__[key] = value


class TestPrivacy(Privacy):
    privates = ['age']
    # def __init__(self):
    #     self.privates =['age'] # can not use self.privates because privates is not in attr __dict__


class Complex(object):
    def __init__(self, real, image):
        self.real = real
        self.image = image
    def __repr__(self):
        return "%s + %si" % (self.real, self.image)

    def __add__(self, other):
        log.info("Using __add__: self=%s, other=%s", self, other)
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.image + other.image)
        else:
            return self
    def __iadd__(self, other):
        log.info("Using __iadd__;if no __iadd__, will use __add__:")
        self.real, self.image = (self.real + other.real, self.image + other.image)
        return self

    def __radd__(self, other):
        log.info("Using __radd__: self=%s, other=%s", self, other)
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.image + other.image)
        else:
            return self


if __name__ == "__main__":
    xsm = XsmCard()
    print isinstance(xsm, Card)
    print isinstance(xsm, XsmCard)
    card = Card()
    print isinstance(card, Card)
    print isinstance(card, XsmCard)
    xsm.dbi_plug_unplug(1, a=2, b=3)
    ptim = PtimCard()
    ptim.do_final_check()
    singleton = _Singleton("singleton")
    log.info("singlen ID: %s", id(singleton))
    del _Singleton
    log.info("After del _Singleton, cannot use it create a new instance, but can get instance by the original class")
    another_singleton = singleton.__class__("another")
    log.info("Another singleton after first del: %s, ID:%s", another_singleton, id(another_singleton))

    hv = HvAccess()
    hv2 = HvAccess()

    tree = 100
    test_global_variable(tree)
    test_default_param(1)
    test_default_param(2)

    person = Person("wang", 30)
    p2 = Person("li", 24)
    p3 = anotherSignle()
    p3.name = "li"
    p3.age = 80
    p4 = anotherSignle()
    p5 = testPerson()
    p5()
    log.info("attribute: %s", person.att)
    log.info(sorted(dir(Person)))
    log.info(sorted(dir(testPerson)))
    log.info("person:name=%s, age=%s, p2:name=%s, age=%s", person.name, person.age, p2.name, p2.age)
    log.info("name, age: %s, %s", p3.name, p3.age)

    contern = Container(1,5)
    for i in contern:
        for j in contern:
            print i,j

    contain = SkipObject("abcdefg")
    for i in contain:
        for j in contain:
            print i, j, '  ',
    print ""
    test = TestPrivacy()
    # test.age = 100

    c1 = Complex(1, 2)
    c2 = Complex(2, 3)
    print c1 + 2
    c1 += c2
    print  2 + c2

