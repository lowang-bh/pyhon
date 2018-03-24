#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 File Name: timeout_decrator.py
 Author: longhui
 Created Time: 2018-03-24 22:18:06
"""

import sys
import time
import threading

class KThread(threading.Thread):
    """A subclass of threading.Thread, with a kill()
    method.

    Come from:
    Kill a thread in Python:
    http://mail.python.org/pipermail/python-list/2004-May/260937.html
    """

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run  # Force the Thread to install our trace.
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
        trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True
class Timeout(Exception):
    """function run timeout"""


def timeout(seconds):
    """超时装饰器，指定超时时间
    若被装饰的方法在指定的时间内未返回，则抛出Timeout异常"""

    def timeout_decorator(func):
        """真正的装饰器"""

        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        def _(*args, **kwargs):
            result = []
            new_kwargs = {  # create new args for _new_func, because we want to get the func return val to result list
                'oldfunc': func,
                'result': result,
                'oldfunc_args': args,
                'oldfunc_kwargs': kwargs
                }
            thd = KThread(target=_new_func, args=(), kwargs=new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            thd.kill()  # kill the child thread
            if alive:
                raise Timeout(u'function run too long, timeout %d seconds.' % seconds)
            else:
                return result[0]

        _.__name__ = func.__name__
        _.__doc__ = func.__doc__
        return _

    return timeout_decorator


import signal,functools #下面会用到的两个库
class TimeoutError(Exception): pass #定义一个Exception，后面超时抛出

def time_out(seconds, error_message = 'Function call timed out', default_ret=None):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            result= default_ret
            try:
                result = func(*args, **kwargs)
            except TimeoutError:
                print "Timeout :", seconds
            finally:
                signal.alarm(0)
            return result
        return functools.wraps(func)(wrapper)
    return decorated


import functools
#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

import functools

#或者针对带参数的decorator：
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@timeout(2)
def methodtimeout(seconds, text):
    print 'start', seconds, text
    time.sleep(seconds)
    print 'finish', seconds, text
    return seconds

@time_out(3)
def method_timeout(seconds, text):
    print 'start', seconds, text
    time.sleep(seconds)
    print 'finish', seconds, text
    return seconds

if __name__ == '__main__':
    for sec in range(1, 5):
        try:
            print '*' * 20, method_timeout.__name__
            print method_timeout(sec, 'test waiting %d seconds' % sec)
        except Timeout, e:
            print e
