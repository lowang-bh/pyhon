#!/usr/local/bin
# _*_ coding: utf-8 _*_
from operator import itemgetter

# 1. 举例说明可变对象和不可变对象都有哪些

# 2. 哪些类型可以作为字典的key, 哪些不可以

# 3. read, readline, readines的区别，怎么使用
"""
read 读取整个文件
readline 读取下一行,使用生成器方法
readlines 读取整个文件到一个迭代器以供我们遍历
"""

# 同理， range and xrange 的区别和使用注意事项

# 4. python中类的3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法，有啥区别，怎么使用？类变量和实例变量呢 ?
class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x
a, x = A(), "hello"
a.foo(x), a.class_foo(x), a.static_foo(x)
A.class_foo(x), A.static_foo(x)

# 5. *args和**kwargs的使用
def print_everything(*args, **kwargs):
    print(args)
    print(kwargs)

print_everything(1,2,3, key="value")
print_everything(*[1,2,3], **{"key":"value"})

# 6. 下面的代码打印值？
Long_Str =  "longlongstringlonglongstring" *2 

def mystr():
    return Long_Str

def printV():
    a = mystr()
    if a is Long_Str * 2:
        print(1)
    else:
        print(0)
printV()        


# 7.  默认参数的问题：不要使用动态类型作为默认参数，因为函数定义的时候确定了参数的值
def test(arg1, args=[]):
    args.append(arg1)
    return args

print(test(1))
print(test(2))

# 8 . 关键字排序, 按value值第二项从小到大排序，如果相同，按第三项从小到大
d = {"a":[11,2,10,4], "b":[2,2,3,4], "c" : [10,9,5,4]}
s = sorted(d.iteritems(), key=lambda (k,v): itemgetter(1,2)(v))
print(s)

l = [[11,2,10,4], [2,2,3,4],  [10,9,5,4]]
print(sorted(l, key=itemgetter(1,2)))

l.sort(key=lambda x: (x[1],x[2]))
print(l)

# 9. 闭包
def mySqure(n):
     return [lambda x: i*x for i in range(n)]
    # return [lambda x, i=i: i*x for i in range(n)]
fs = mySqure(5)
for func in fs:
    print(func(2))
        
