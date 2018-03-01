#/usr/bin/env python

from oneThread import loop0, loop1
from time import sleep, ctime
import thread

def main():
    print 'starting at time:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(10)
    print 'all DONE at time:', ctime()
    
if __name__ == '__main__':
    main()
    