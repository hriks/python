def fibinacci(a, b, i):
    counter = 0
    print a, b,
    while (counter < i):
        value = a + b
        a = b
        b = value
        counter = counter + 1
        print value,


fibinacci(0, 1, 10)

