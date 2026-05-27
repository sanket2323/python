def find_remainder(a, b):
    return [a // b, a % b]


print(find_remainder(6, 3))


def second_largest_number(a, b, c):
    return a + b + c - max(a, b, c) - min(a, b, c)


print(second_largest_number(20, 30, 40))


def swap_number(x, y):
    x = x + y
    y = x - y
    x = x - y

    return x, y


print(swap_number(100, 200))
