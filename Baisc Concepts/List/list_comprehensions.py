def sortPeople( names, heights)  :
    dict_names = dict(zip(heights, names))
    dict_names = sorted(dict_names.items(), key=lambda x: x[0], reverse=True)
    print(type(dict_names))

    final_output = [x[0] for x in dict_names]
    return final_output


names = ["Mary","John","Emma"]
heights = [180,165,170]

print(sortPeople(names,heights))

