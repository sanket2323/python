def char_index(text: str):
    ans = {}

    for k, char in enumerate(text):

        if char in ans:
            ans[char].append(k)

        else:
            ans[char] = [k]

    return ans


print(char_index('sanketdt'))
