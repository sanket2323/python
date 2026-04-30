# zeroDivisionError any number divided by zero will give us this error.
# valueError: If we try to convert any value to required form. trying to convert pizza to int.
# typeerror : happens during operation while variable are of not same type

#it mostly used during the input statement cuz user can enter anything

try:
    num_guess = int(input("Enter the number of guess: "))
    print(1/num_guess)
except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("Invalid input")
finally:
    print("Goodbye")
    #it usefull for clean up


# #1
# If input is not a number → handle error
# If age < 0 → raise exception
# If age > 120 → raise exception
# Always print "Program ended" at the end

try:
    get_age = int(input("Enter the age: "))
    if 0 > get_age > 120:
        print("Invalid age")
    else:
        print("Age is valid")
except ValueError:
    print("Invalid input")
finally:
    print("Goodbye")