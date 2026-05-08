from book import *
from user import *
from admin import *
print("this file is read")
admin1 = Admin()

admin1.add_book(23)
admin1.add_book(24)

admin1.display_all_books(admin1.book_list)
admin1.search_book("sanket",admin1.book_list)



