frutis = ["apple","mango","banana","Goa","santra","Pineapple"]

#1
for index, value in enumerate(frutis):
    print(value)
print("-----------------------------")
#2
for index ,value in enumerate(frutis):
    if(index % 2 == 0):
        print(value)
print("-----------------------------")
#3
for index, value in enumerate(frutis,start=100):
    print(value)
    print(index)
