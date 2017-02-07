print "Enter the number pls"
b = int(input())
print "Factorial is",


def asd(n):
    if (n == 1):
        return 1
    else:
        return (n * asd(n - 1))

print "This is your's desired no",asd(b)
