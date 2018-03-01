#!/usr/bin/env python
"readTextFile.py --read and display text file"

import os

def display_file_content(fname=None):
	if not fname:
		fname = raw_input("Enter filename:")
	print fname
	# attemp to open file and display
	try:
		fobj = open(fname, 'r')
	except IOError, e:
		print "***file open error:", e
	else:
		print fobj
		for eachline in fobj:
			print eachline.strip(),
		fobj.close()
	

def merge_two_file(file1, file2):
	try:
		fobj1 = open(file1)
		fobj2 = open(file2)
	except IOError, e:
		print "str(e)"
	
	lines1 = fobj1.readlines()
	lines2 = fobj2.readlines()
	index = 0
	for line in lines1:
		line = "#[[" + line.split('/')[-1].split('.')[0] + ' | ' + lines2[index].rstrip() + "]"
		print line
		index += 1


if __name__ == "__main__":
	merge_two_file("file1.txt", "file2.txt")
