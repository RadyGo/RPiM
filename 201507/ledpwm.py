#!/usr/bin/python

led0 = open('/dev/rtled0', 'a')
n = 0

while True :
	print >> led0, "%d" % (0 if n%5 else 1)
	n = n + 1
