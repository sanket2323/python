def majorityElement( nums) -> int:
    ans = {}

    for num in nums:
        ans[num] = ans.get(num, 0) + 1
    print(ans)
    max_value = max(ans.values())
    print(max_value)

    for num in ans:

        if ans[num] == max_value:
            return num
    return -1

print(majorityElement([3,2,3]))

class Clicker():
    _all_clicks = 0
    def __init__(self): self._clicks = 0
    def click(self):
        self._clicks += 1
        Clicker._all_clicks += 1



c = Clicker(); d = Clicker()
c.click(); c.click()
d.click()
print(c.all_clicks)