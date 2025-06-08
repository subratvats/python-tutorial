def my_function():
  print("Hello from a function")

# Calling the function
my_function()  # Output: Hello from a function

# Function with parameters
def my_function(fname):  #parameter
  print(fname + " Refsnes")

my_function("Emil")  # argument passes
my_function("Tobias")
my_function("Linus")

# If you do not know how many arguments that will be passed into your 
# function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# If you do not know how many keyword arguments that will be passed into
# your function, add two asterisk: ** before the parameter name in 
# the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Function with default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")  # Output: I am from Sweden
my_function("India")  # Output: I am from India
my_function()  # Output: I am from Norway (default value)

# Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)
  
fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# return value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))