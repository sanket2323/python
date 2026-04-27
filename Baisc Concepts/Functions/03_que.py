import math

def circle(r):
    area = math.pi * r ** 2
    perimeter = 2 * math.pi * r
    return area, perimeter

a, c = circle(3)

print(a)