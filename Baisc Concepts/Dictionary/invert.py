def invert(d:dict):

    ans = {}

    for key in d:

        value = d[key]

        if value in ans:
            ans[value].append(key)

        else:
            ans[value] = key

    return ans
dic ={1: 10, 2: 10}

print(invert(dic))