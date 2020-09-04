
# _*_ coding: utf-8 _*_


class DummyResource:
    def __init__(self, tag):
        self.tag = tag
        print 'Resource [%s]' % tag
        
    def __enter__(self):
        print '[Enter %s]: Allocate resource.' % self.tag
        raise Exception("enter exception")
        return self # 可以返回不同的对象
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        
        print '[Exit %s]: Free resource.' % self.tag
        if exc_tb is None:
            print '[Exit %s]: Exited without exception.' % self.tag
        else:
            print '[Exit %s]: Exited with exception raised.' % self.tag
            print(exc_type)
            print(exc_value)
            print(exc_tb)
            return False    # 可以省略，缺省的None也是被看做是False


# with DummyResource('Normal'):
#     print '[with-body] Run without exceptions.'

with DummyResource('With-Exception'):
    print '[with-body] Run with exception.'
    a= 1/0
    print '[with-body] Run with exception. Failed to finish statement-body!'
