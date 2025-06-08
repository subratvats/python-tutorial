# In OOP, you create objects. Each object can store data and have 
# functions that work with that data.

class MyClass:
    x= 5
    
o1 = MyClass()  # Create an object of MyClass
print(o1.x)  # Output: 5
print(MyClass)  # Output: <class '__main__.MyClass'>
print(MyClass.x)  # Output: 5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)  # Create an object of Person
print(p1.name)  # Output: John
#  with str method 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)


# object methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old.")

p1 = Person("John", 36)  # Create an object of Person
p1.myfunc()  # Call the method myfunc of the object p1

p1.age = 40

print(p1.age)
p1 = Person("John", 36)

del p1.age

print(p1.age)
# You can delete objects by using the del keyword:
p1 = Person("John", 36)

del p1

print(p1)
