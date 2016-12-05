print "Enter the number pls"
b = int(input())
print "Factorail is",


def asd(n):
    if (n == 1):
        return 1
    else:
        return (n * asd(n - 1))


print asd(b)
