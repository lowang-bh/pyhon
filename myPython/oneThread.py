#/usr/bin/env python

from time import sleep, ctime
print "test import"

def loop0():
    print 'start loop0 at time:', ctime()
    sleep(4)
    print 'loop0 done at time:', ctime()
    return
    
def loop1():
    print 'start loop1 at time:', ctime()
    sleep(2)
    print 'loop1 done at time:', ctime()
    return

def main():
    print 'starting at time:', ctime()
    loop0()
    loop1()
    print 'all DONE at time:', ctime()
    
if __name__ == '__main__':
    main()
    