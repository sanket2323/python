matrix = [
    [1, 2, 3],
    [2, 2, 5]
]

target = 2


def count_target(matrix, target) -> int:
    count = 0
    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if matrix[i][j] == target:
                count += 1
    return count


print(count_target(matrix, 2))
