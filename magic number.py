def sum_digits(n):
    num = 0
    s = 0
    p = 0
    while n:
        s += n % 10
        print s, 'n%10 ', n % 10
        n //= 10
    b = s
    while b:
        num = ((10 * num) + (b % 10))
        b //= 10
    print num, s
    p = num * s
    print p
    if (p == n):
        print "Magic Number"
    else:
        print "Not a magic number"
    return s
    return num


print sum_digits(1459)
