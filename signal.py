#!/usr/bin/env python
import signal
import time
def my_handler(signum, frame):
    print "I received:", signum

def int_handler(signum, frame):
    print "I received:", signum, frame
    exit(0)
signal.signal(signal.SIGALRM, my_handler)
signal.signal(signal.SIGINT, int_handler)
signal.alarm(5)
while True:
    print "not yet"
    time.sleep(0.5)
