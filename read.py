# /usr/bin/env python
'read a file content'

#get the filename
fname = raw_input('Enter the file name: ')

print fname

try :
	fobj = open( fname, 'r')
except IOError, e:
	print "*** file open Error:", e
else: 
	#display the content
	for eachLine in fobj:
		print eachLine,
fobj.close()
