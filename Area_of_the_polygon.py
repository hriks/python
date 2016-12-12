import math
def polygon(sides, length):
    pie = 3.14159
    nume = sides * (length ** 2)
    deno = 4 * math.tan ( pie / sides)
    val = nume / deno
    return val

   
print polygon(7, 3)
