def combine(dict1, dict2):
    ans ={}
    for key in dict1:

        if key in dict2:
            ans[key] = sum(dict1[key]) + sum(dict2[key])


    return ans


print(combine({1: [2], 4: [5, 6]}, {4: [8]}))

