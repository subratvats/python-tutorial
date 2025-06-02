x='subrat vats'
print(x)      
print(type(x))  # <class 'str'>
print(id(x))    # address of x

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
myVariableName = "John" #camelCase
my_variable_name = "John" #snake_case
MyVariableName = "John"

# Multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# printing multiple variables using comma
x = 5
y = "John"
print(x, y)

#Global variables
x = "awesome"

def myfunc():
  global y
  y = "fantastic"  # change the global variable x
  print("Python is " + x)

myfunc()
print("Python is " + y)


import random

print(random.randrange(1, 10))
print(random.randbytes(5))  # returns a random byte string of length 5