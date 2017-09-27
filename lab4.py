import re

f = open("mbox-short.txt", "r")
for x in f:
	l = x.strip()
	if re.findall("From", l):
		numbers = re.findall("[0-9]+", l)
		name = re.findall("(\S+)@", l)
		print (numbers)
		print (name)
