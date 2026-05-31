def vowel_frequency(word: str):
    ans = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for char in word:

        if char in ans.keys():
            ans[char] += 1

    return ans
print(vowel_frequency("programming"))