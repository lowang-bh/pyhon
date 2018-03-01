import sqlite3, time, os, sys, atexit, threading
from optparse import OptionParser
import message

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
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter("%(asctime)s,%(lineno)4d : %(message)s"))
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
#     def do_final_check(self):
#         logging.info("do_final_check: in XsmCard Class")

class LineCard(Card):
    def __init__(self):
        super(LineCard, self).__init__()
        
    def do_final_check(self):
        logging.info("do_final_check: in LineCard Class")
        
class PtimCard(XsmCard, LineCard):
    def __init__(self):
        super(PtimCard, self).__init__()
    def do_final_check(self):
        XsmCard.do_final_check(self)
        logging.info("do_final_check: in PtimCard Class")

def test_global_variable(root):
    print "root=%s" % tree
    
def test_default_param(n, l=[], d={}):
    l.append(n)
    d[n] = n
    print l, d
    return l

class _Singleton(object):
    def __init__(self, name=None):
        self.name = name
        print "name=%s" % name

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
            return instance

        # need to double check the instance. it's double check
        with cls.instance_lock:

            instance = cls.__dict__.get("__it__")
            if instance is not None:
                return instance
            cls.__it__ = instance = object.__new__(cls)

            log.info("got new lock for hv_access and return")

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
    del _Singleton
    another_singleton = singleton.__class__()

    hv = HvAccess()
    hv2 = HvAccess()

    tree = 100
    test_global_variable(tree)
    test_default_param(1)
    test_default_param(2)
