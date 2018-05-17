#!/usr/bin/env python
import signal
import time
import os


def my_handler(signum, frame):
    print "I received:", signum


def int_handler(signum, frame):
    print "I received:", signum, frame
    exit(0)


def term_handler(signum, frame):
    print "Received terminal signal:", signum
    exit(0)


print signal.getsignal(signal.SIGALRM)
print signal.signal(signal.SIGALRM, my_handler)
print signal.SIG_DFL
signal.signal(signal.SIGINT, int_handler)
signal.signal(signal.SIGTERM, term_handler)
signal.alarm(4)
num = 0
pid = os.getpid()
while True:
    print "not yet", num, pid
    time.sleep(0.5)
    num += 1
    if num >= 8:
        num = 0
        signal.alarm(0)
        # signal.signal(signal.SIGALRM, signal.SIG_DFL)
        print signal.alarm(2)
