def word_frequency(sen: str):
    list_words = sen.split()
    ans = {}

    for word in list_words:

        if word in ans:
            ans[word] += 1

        else:
            ans[word] = 1

    return ans


print(word_frequency("cat dog cat fish dog cat"))
