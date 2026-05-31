def uppercase_frequency(text: str):
    ans = {}

    for char in text:

        if char.isupper():
            ans[char] = ans.get(char, 0) + 1  # imp concept

    return ans


print(uppercase_frequency("HeLLo"))
