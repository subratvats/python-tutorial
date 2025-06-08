# if-else statement 
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
# Output: x is greater than 5

# pass statement
a = 33
b = 200

if b > a:
  pass

# shorthand if statement
a = 2
b = 330
print("A") if a > b else print("B")  # Output: B


# shorthand if-else statement with multiple conditions
a = 2000
b = 2000
print("A") if a > b else print("=") if a == b else print("B")  # Output: B

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions is True")
if not b > a:
  print("a is NOT greater than b")