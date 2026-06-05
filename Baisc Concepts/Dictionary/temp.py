def majorityElement(nums) -> int:
    ans = {}

    for num in nums:
        ans[num] = ans.get(num, 0) + 1

    max = 0
    for num in ans:
        if max < ans[num]:
            max = ans[num]

    for num in ans:
        if ans[num] == max:
            return num

    return None

nums = [3,2,3]
print(majorityElement(nums))
