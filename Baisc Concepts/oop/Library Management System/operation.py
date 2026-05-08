from admin import *
class Operations:

    def __init__(self):
        self.admin = Admin()

    def print_options(self):
        print("Operation which can be done")
        list_of_operations = [
            '1. Add book',
            '2. Delete book',
            '3. Display all book',
            '4. Search Book'
        ]
        for operation in list_of_operations:
            print(operation)
        return self.get_user_choice(len(list_of_operations))
            
        
    def get_user_choice(self,list_length) -> int:
        while True:
            try:
                user_choice = int(input(f"Select a option between range 1 and {list_length}:"))
                if 1<= user_choice <= list_length:
                    return user_choice
                
                print("Out of Range! select again")
                   
            except ValueError:
                print("user must enter a integer.")
                
        
            
            
ope = Operations()
ope.print_options()

