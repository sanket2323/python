names = ["sanket","sohan","shreya","shruti"]

#1 
def toUpperCase(name:str):
    return name.upper()

new_Upper_list = list(map(toUpperCase,names))
print(new_Upper_list)
