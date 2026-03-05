while True:
    positive_interger = int(input("Enter the positive number:"))
    if(positive_interger >= 0):
        break
    
x = 0

while (x <= positive_interger):
    powered_value = 2 ** x
    print(f"{x} {powered_value}")
    x += 1
    
    
    
