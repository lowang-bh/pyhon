#!/usr/bin/env python
"MakeTextFile.py -- create text file"

import os
ls = os.linesep
#get filename
while True:
	fname=raw_input("Input you file name to create:")
	if os.path.exists(fname):
		print "ERROR: '%s' already exists " %fname
	else:
		break;
	
#get file content lines
all=[]
print "\n input lines ('.' by itself to quit).\n"

#loop until user terminates
while True:
	entry = raw_input('>')
	if  entry == '.':
		break
	else:
		all.append(entry)
#write to file
fobj=open(fname, 'w')
fobj.writelines(['%s%s'%(x,ls) for x in all])
fobj.close()
print "Done!"

	