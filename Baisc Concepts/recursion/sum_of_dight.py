def sum_of_dight(num:int):
    sum = 0
    if num == 0:
        return 0

    return num % 10 + sum_of_dight(num//10)

print(sum_of_dight(123))