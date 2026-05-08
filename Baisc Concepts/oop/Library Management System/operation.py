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
            '4. Search Book',
            '5. Exit'
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
                
    def add_book(self):
        while True:
            try: 
                book_id = int(input("Enter the book id"))
                self.admin.add_book(book_id)
                break
            except ValueError:
                print("Book id must be interger")
                
    def delete_book(self):
        while True:
            try: 
                book_id = int(input("Enter the book id"))
                self.admin.add_book(book_id)
                break
            except ValueError:
                print("Book id must be interger")
        book_list = self.admin.book_list
        self.admin.delete_a_book(book_id,book_list)
        
    def display_books(self):
        book_list = self.admin.book_list
        self.admin.display_all_books(book_list)
        
    def search_book(self):
        book_list = self.admin.book_list
        book_name = input("Enter the book name you want to search:")
        self.admin.search_book(book_name,book_list)
                
    def run(self):
        
        while True:
            user_choice = self.print_options()
            
            if user_choice == 1:
                self.add_book()
            
            elif user_choice == 2:
                self.delete_book()
            
            elif user_choice == 3:
                self.display_books()
            
            elif user_choice == 4:
                self.search_book()
            
            elif user_choice == 5:
                exit
            
            break
        
        print("Thanks for using Library Management System")
                  
