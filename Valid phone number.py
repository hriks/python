import re
n = int(raw_input())
for i in range(0, n):
    number = raw_input()
    validPhoneNumber = re.compile("[7-9]\d{9}")
    if len(number) == 10 and validPhoneNumber.match(number):
        print "YES"
    else:
        print "NO"
# Checks the effective phone number
