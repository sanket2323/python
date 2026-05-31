def students_with_mark(marks,target):
    names = []
    for name in marks:

        if marks[name] == target:
            names.append(name)

    return names

print(students_with_mark(
    {
        'sanket':90,
        'sharu':90,
        'ali':90
    },
    90
))