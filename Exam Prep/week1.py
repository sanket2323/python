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

print(2 + 3 * 4 ** 2)

num = 572

def extract_number(number):

    hund_place = number // 100
    tenth_place = (number // 10) % 10
    first_place = number % 10

    return hund_place, tenth_place,  first_place

print(extract_number(num))

cs = "0123456789"

print(int(3.14))

matrix = [
    [1,2,3],
    [4,5,6]
]
#
final_out = []

def transpose(matrix: list[list[int]]) -> list[list[int]]:

    cols = len(matrix)
    rows = len(matrix[0])

    ans = []

    for j in range(cols):

        new_row = []

        for i in range(rows):

            new_row.append(matrix[i][j])

        ans.append(new_row)

    return ans

print(transpose(matrix))

