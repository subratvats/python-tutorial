class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
print("==========================")

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("subrat", "vats")
x.printname()  # Output: Mike Olsen
print("==========================")

# super() function
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)  # Call the parent's __init__() function
x = Student("subrat", "vats")
x.printname()  # Output: subrat vats

# Note: The super() function is used to give access to methods and properties of a parent or sibling class.
# It returns a temporary object of the superclass that allows
# you to call its methods and properties.
# super() is often used in the __init__() method to call the parent's __init__() method.
# super() can also be used to call other methods of the parent class.
# It is a built-in function that returns a proxy object that delegates method calls to a parent or sibling class.
# super() is useful in multiple inheritance scenarios, where you want to call methods from multiple parent classes.
# super() can be used to access methods from a parent class without explicitly naming it.
# It is commonly used in class inheritance to ensure that the parent class's methods are called correctly.

# Add Properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
#   def __init__(self, fname, lname):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)  # Call the parent's __init__() function
    self.graduationyear = year  # Add a new property
# x = Student("subrat", "vats")
x = Student("subrat", "vats", 2024)
x.printname()  # Output: subrat vats
print(x.graduationyear)  # Output: 2023

# add methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # Call the parent's __init__() function
        self.graduationyear = year  # Add a new property
    
    def welcome(self):  # Add a new method
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("subrat", "vats", 2024)
x.printname()  # Output: subrat vats
x.welcome()  # Output: Welcome subrat vats to the class of 2024

