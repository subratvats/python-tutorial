# A lambda function is a small anonymous function.

# A lambda fun can take any number of arguments,4 but can only have one expression.
# Syntax
# lambda arguments : expression

x = lambda a, b, c: a + b + c
print(x(5, 3, 3))  # Output: 8


def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
print(mydoubler(11))  # Output: 22
# ===============
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
# Use lambda functions when an anonymous function is required for a 
# short period of time.

