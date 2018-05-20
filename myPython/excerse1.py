# coding: utf-8
def is_loop_str(myinput):
    if isinstance(myinput, int):
        mystr = str(myinput)
    elif isinstance(myinput, str):
        mystr = myinput
    else:
        print("Error, input not a string or an integer")
        return False
    reverse_list= list(mystr)
    reverse_list.reverse()
    if mystr == "".join(reverse_list):
        return True
    else:
        return False

print is_loop_str(12321)
print is_loop_str("abkadsn")
print is_loop_str([1,2,1])

class Phone(object):
    def __init__(self, screen_size, price, brand):
        self._screen_size = screen_size
        self._price = price
        self._brand = brand

    @property
    def screen_size(self):
        return self._screen_size
    @screen_size.setter
    def screen_size(self, size):
        self._screen_size = size

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = price

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    def play(self):
        print("play game")
    def sendMessage(self):
        print("text message")
    def powerOff(self):
        print("power off")
    def get_info(self):
        print(self.screen_size, self.price, self.brand)

phone1=Phone(5.5, 6288, 'Apple')
phone2=Phone(5, 1999, 'mi')
phone1.play()
phone1.sendMessage()
phone1.powerOff()
phone1.get_info()
phone1.price=8799
phone1.screen_size=6.0
phone1.get_info()



class cinema(object):
    total_sales=0
    def __init__(self, name, location, sales):
        self.name = name
        self.localation = location
        self.sales = sales
        cinema.total_sales += sales

    @classmethod
    def getSales(cls):
        return cls.total_sales
    def saleTickests(self, price, number):
        self.sales += price *number
        cinema.total_sales += price * number


c1=cinema('wanda','beijing',1000)
c2=cinema('wanda','guangzhou',2000)
c1.saleTickests(50,2)
c2.saleTickests(100,3)
print cinema.getSales()

class miniCinema(cinema):
    def __init__(self, name, localtion, sales):
        super(miniCinema, self).__init__(name, localtion, sales)

    def saleTickests(self, price, number):
        if price > 100:
            price = 0.9 * price

        self.sales += price *number
        cinema.total_sales += price * number
c3=miniCinema("wangda","shenzhen",0)
c3.saleTickests(120,2)
print c3.getSales()

s = "string in global"
num = 99
def numFunc(a, b):
    num = 100
    print "print s in numFunc: ", s

    def addFunc(a, b, c):
        s = "string in addFunc"
        print "print s in addFunc: ", s
        print "print num in addFunc: ", num
        print "locals of addFunc: ", locals()
        print
        return "%d + %d = %d" % (a, b, a + b)

    print "locals of numFunc: ", locals()
    print
    return addFunc

t=numFunc(3, 6)
print "globals: ", globals()
t(4,9,10)


def greeting_conf(prefix):

    def greeting(name):
        print prefix, name

    return greeting

mGreeting = greeting_conf("Good Morning")
mGreeting("Wilber")
mGreeting("Will")
print "function name is:", mGreeting.__name__
print "id of mGreeting is:", id(mGreeting)

print dir(mGreeting)
print mGreeting.__closure__
print type(mGreeting.__closure__)
print type(mGreeting.__closure__[0])
print mGreeting.__closure__[0].cell_contents

aGreeting = greeting_conf("Good Afternoon")
print "function name is:", aGreeting.__name__
print "id of aGreeting is:", id(aGreeting)


try:
    import __builtin__ as b
except:
    pass
    # python3
    #import builtins as b
