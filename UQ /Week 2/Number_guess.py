import random

random_number = random.randint(1,100)
print(random_number)
while True:
    user_number = int(input("Enter the number:"))
    
    if(user_number == random_number):
        print("Congratulations!")
        break
    else:
        print("Sorry that is not correct.")
        
        
