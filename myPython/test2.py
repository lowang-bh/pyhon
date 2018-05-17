from myPython.tes1 imptort myclass

def another(name):
    t=myclass()
    ret = t.get_name(name)
    print ret
    call_class_test(t)
    t.call_function(t)
def call_class_test(myclass):
    print "in call class test"
