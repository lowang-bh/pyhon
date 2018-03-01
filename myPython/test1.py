class myclass():
    def __init__(self):
        self.element="I am in original myclass"
        print "init"
    def get_name(self,name):
        print "in get_name"
        return name
    def call_function(self,callclass):
        callclass.get_name(self.element)