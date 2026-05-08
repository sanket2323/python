class User:
    def __init__(self):
        self.id = None
        self.name = None
        self.user_info()

    def user_info (self):
        while True:
            try:
                self.id = int(input("Enter user id: "))
                break
            except ValueError:
                print("User id must be an integer")

        self.name = input("Enter user name: ")