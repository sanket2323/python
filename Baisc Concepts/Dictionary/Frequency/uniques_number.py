def firstUniqChar( s: str) -> int:
    ans = {}

    for char in s:
        ans[char] = ans.get(char, 0) + 1

    print(ans)
    char = []
    for char in s:

        if ans[char] == 1:
            char.append(char)

    for i in range(len(s)):

        if s[i] == char:
            return i

    return -1

print(firstUniqChar('leetcode'))