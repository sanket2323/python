nested_list = [[0,1,2],[3,4,5]]

print(nested_list[0][0])
print(nested_list[1])
print(nested_list[1][2])

print("==============================")
for row in nested_list:
    print(row)
    for element in row:
        print(element)
        
print("==============================")

x = 0
while x < len(nested_list):
    print(nested_list[x])
    y = 0
    while y < len(nested_list[x]):
        print(nested_list[x][y])
        y += 1
    x += 1
    

def multiply(num1 : int , num2 :int ):
    output = num1 * num2 
    return output

x = multiply(3,'python')
print(x)

print(bool(True or a))

xs = ['A','B']
ys = 2 * xs
print(ys)

for k in range(6):
    print(k)
    
print("Printed statement added")