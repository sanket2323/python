def reverse_lookup(d,text):
    ans_index = []
    ans_key = []

    for index,key in enumerate(d):

        # if d[key] == text:
        #     ans_index.append(index)

        if d[key] == text:
            ans_key.append(key)

    return ans_key

a = reverse_lookup({1: "bluey", 19: "chilli", -31: "bluey"}, "bluey")
print(a)