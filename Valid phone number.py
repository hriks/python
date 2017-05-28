import re
number = raw_input()
validPhoneNumber = re.compile("[7-9]\d{9}")
if len(number) == 10 and validPhoneNumber.match(number):
    print "YES"
else:
    print "NO"
    for n in number:
    	if n == ("[7-9]\d{9}"):
    		n.pop()
    print number
# Checks the effective phone number
