  # -*- coding: utf-8 -*-
print "中文测试"
import re
import os, sys
import sqlite3 as sqlite
from optparse import OptionParser
def main():  
    usage = "usage: %prog [options] arg"  
    parser = OptionParser(usage)  
    parser.add_option("-f", "--file", dest="filename", help="read data from FILENAME")  
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose")  
    parser.add_option("-q", "--quiet",action="store_false", dest="verbose")  
      
    (options, args) = parser.parse_args() 
	
    # if len(args) != 1: 
        # #parser.error("incorrect number of arguments") 
		# print "len=",len(args),"args=%s" %args
    if options.verbose:  
        print "reading %s..." % options.filename  
	print len(args),"args=%s" %args
      
parser=OptionParser()
parser.add_option("-r","--re",action="store_false",dest="verbose")
parser.add_option("-f", "--file", action="store_const",dest="filename", const="name",help="read data from FILENAME")  
parser.add_option("-v", "--verbose", action="store_true", dest="verbose")  
parser.add_option("-q", "--quiet",action="store_false", dest="verbose")
(options, args) = parser.parse_args()
print len(args), args, options.verbose,options.filename
print os.path.basename(sys.argv[0])

con = sqlite.connect("mydb")

text = "Goo is a handsome boy, he is cool, clever, and handsome so on..."
#patten=r"\shandsome\s"
patten=r"(\w+)\s"
m = re.match(patten,text)
if m:
	print m.group(0) 
else:
	print "not match"
	
m = re.search(patten,text)
if m:
	print "search result:", m.groups()
	print m.group(0), m.group(),m.groups()[0],m.group(1)
else:
	print "not search"
print re.sub(r'\s+', '_', text) 
print re.sub(r"\s", lambda m: '['+m.group(0)+']',text,0)

print text

regex =re.compile(r'\w*oo\w*')
myRe=re.compile(r'(boy)|(cool)')
str=['I am a boy','it is so cool']
for x in str:
	res=myRe.search(x)
	if res:
		print "res",res.group(0) 
print regex.findall(text)


yesReg=re.compile(r'[yY]|([yY][eE][sS])')
noReg =re.compile(r'[nN]|([nN][oO])')
myReg =re.compile(r'^([yYnN]$)|^([yY][eE][sS])$|^([nN][oO])$')

while True:
    input=raw_input("input yes or no:")
    res=myReg.search(input)
    if res:
        print res.group(0)
    else:
        print "No match,input error"
        exit(1)
    

if __name__ == "__main__":  
    main() 
