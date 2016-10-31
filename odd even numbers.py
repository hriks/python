def odd_even(li):
    for i in range(0, len(li)):
        if li[i] % 2 == 0:
            print li[i], "even"
        else:
            print li[i], "odd"


lis = [1, 2, 3, 4, 5]
odd_even(lis)
