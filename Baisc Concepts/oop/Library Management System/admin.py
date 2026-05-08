from book import *


class Admin:

    def __init__(self):
        self.book_list = []
        self.user_list = []

    def add_book(self, book_id):
        for item in self.book_list:

            if item.book_id == book_id:
                print("Book already exists")
                return
        title = input("Enter book title: ")
        while True:
            try:
                quantity = int(input("Enter book quantity: "))
                break
            except ValueError:
                print("Quantity must be an integer")
        new_book = Book(book_id, title, quantity)
        self.book_list.append(new_book)
        print("Book added")


    def display_all_books(self,b_list):
        self.book_list = b_list
        for i in range(len(b_list)):
            print(f"Book with id {b_list[i].book_id} is {b_list[i].book_title} ")

    def search_book(self, name,b_list):
        self.book_list = b_list
        book_found = False
        for i in range(len(b_list)):
            if name == b_list[i].book_title:
                print(f"Book with title {b_list[i].book_title} has found")
                print(f"The id of the book is {b_list[i].book_id}")
                book_found = True

        if not book_found:
            print("Book doesn't exist")
    
    def delete_a_book(self,book_id,b_list):
        self.book_list = b_list
        
        for i in range(len(b_list)):
            if b_list[i].book_id == book_id:
                b_list.pop(i)
                print(f"Book with {book_id} removed from Books List")
                break