#! /usr/bin/env python
"this is a test module"
import os
ls = os.linesep
while True :
	# get filename	
	fname = raw_input('Enter filename: ')

	if os.path.exists(fname) :
		print "EORRR: '%s' already exists" % fname
	else :
		break

all = []

print "\nEnter lines ('.' by itself to quit).\n"

#loop to get the content the new create file

while True :
	entry = raw_input('> ')
	if entry == '.' :
		break
	else :
		all.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()

print 'DONE!'
	
