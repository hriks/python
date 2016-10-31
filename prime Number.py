def check_prime(number):
    print number
    if (number == 1):
        return "Not Prime"
    for i in range(2, number / 2):
        if (number % i) == 0:
            return "Composite"
    return "Prime"


lis = [1, 2, 3, 4]
print check_prime(21)
