def three_sum(array, target):
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1

        while left < right:
            sum_of_values = array[i] + array[left] + array[right]
            if target == sum_of_values:
                return [array[i], array[left], array[right]]

            elif target < sum_of_values:
                right -= 1

            else:
                left += 1

    return []

print(three_sum([1, 2, 4, 6, 8],12))
