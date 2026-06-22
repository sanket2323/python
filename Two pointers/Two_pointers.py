# Find a pair that sums to target

def sum_target(a, target):
    left = 0
    right = len(a) - 1

    while left < right:
        res = a[left] + a[right]
        if res == target:
            return a[left], a[right]

        elif res < target:
            left += 1
        right -= 1

    return None

print(sum_target([1, 2, 3, 4, 5, 6], 3))
