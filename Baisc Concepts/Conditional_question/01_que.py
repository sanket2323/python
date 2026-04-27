user = int(input("Provide me Age"))

if user < 13:
    print("child")
elif user < 20:
    print("Teenager")
elif user < 60:
    print("adult")
else:
    print("Senior")