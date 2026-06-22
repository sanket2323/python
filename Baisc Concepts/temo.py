def thirdMax( nums) -> int:
    first = second = third = 0
    if len(nums) < 3:
        return max(nums)

    for num in nums:

        if num > first:
            second, third = third, second

            second = first
            first = num

        elif num < first and num < second:
            third = num

    return third

nums = [1,2,3]
print(thirdMax(nums))