mylist = ["apple", "banana", "cherry"]
print(mylist)  # Output: ['apple', 'banana', 'cherry']
print(type(mylist))
# List items are ordered, changeable, and allow duplicate values

list1 = ["abc", 34, True, 40, "male"]
print(list1)  # Output: ['abc', 34, True, 40, 'male']
list2 = list(("apple", "banana", "cherry"))  # list constructor
print(list2)  # Output: ['apple', 'banana', 'cherry']

# Accessing list items
print(list1[0])  # Output: 'abc'
print(list1[1:3])  # Output: [34, True] 
print(list1[-1])  # Output 'male' (last item)
print(list1[-2])  # Output: 40 (second last item)

# Changing list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Changing a range of items
thislist = ["apple", "banana", "cherry"]    
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # Output: ['apple', 'blackcurrant', 'watermelon', 'cherry']

# Inserting items
thislist = ["apple", "banana", "cherry"]    
thislist.insert(1, "orange")  # Insert "orange" at index 1
print(thislist)  # Output: ['apple', 'orange', 'banana', 'cherry']

# Appending items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Extending lists
thislist1 = ["apple", "banana", "cherry"]   
thislist2 = ["orange", "kiwi", "melon"]
thislist1.extend(thislist2)  # Extend list1 with list2
print(thislist1)  # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']    
# Adding items from another iterable
# The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).
thislist1 = ["apple", "banana", "cherry"]       
thislist2 = ("orange", "kiwi", "melon")  # Tuple
thislist1.extend(thislist2)  # Extend list1 with tuple
print(thislist1)  # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

#removing items
thislist = ["apple", "banana", "cherry", "banana"]    
thislist.remove("banana")
print(thislist)  # Output: ['apple', 'cherry', 'banana'] (only the first occurrence is removed)

# Removing an item by index
thislist = ["apple", "banana", "cherry"]    
del thislist[1]  # Remove the item at index 1
print(thislist)  # Output: ['apple', 'cherry']  
# Removing the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()  # Removes the last item
print(thislist)  # Output: ['apple', 'banana']
# Removing an item by index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # Removes the item at index 1
print(thislist)  # Output: ['apple', 'cherry']
# Clearing a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()  # Removes all items from the list
print(thislist)  # Output: [] (empty list)


# Looping through a list
thislist = ["apple", "banana", "cherry"]    
for item in thislist:
    print(item)  # Output: apple, banana, cherry (each on a new line)

for i in range(4,7,2):  # Looping through a range
    print(i)

# looping through a list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
print("----")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]  # List comprehension to filter items
print(newlist)  # Output: ['banana', 'mango']
[print(x) for x in fruits if "a" in x]
# newlist = [expression for item in iterable if condition == True]

# List comprehension with condition
newlist = [x for x in range(10) if x < 5]  # List comprehension with condition  
print(newlist)  # Output: [0, 1, 2, 3, 4]
# List comprehension with condition and transformation  
newlist = [x if x < 5 else "greater than 5" for x in range(10)]  # List comprehension with condition and transformation
print(newlist)  # Output: [0, 1, 2, 3, 4, 'greater than 5', 'greater than 5', 'greater than 5', 'greater than 5', 'greater than 5']

#sort list
thislist = ["apple", "banana", "cherry"]    
thislist.sort()  # Sorts the list in ascending order
print(thislist)  # Output: ['apple', 'banana', 'cherry']

# Sorting in reverse order
thislist = ["apple", "banana", "cherry"]        
thislist.sort(reverse=True)  # Sorts the list in descending order
print(thislist)  # Output: ['cherry', 'banana', 'apple']

# Sorting a list of numbers
thislist = [100, 50, 65, 82, 23]    
thislist.sort()  # Sorts the list in ascending order
print(thislist)  # Output: [23, 50, 65, 82, 100]
# Sorting a list of numbers in reverse order
thislist = [100, 50, 65, 82, 23]    
thislist.sort(reverse=True)  # Sorts the list in descending order
print(thislist)  # Output: [100, 82, 65, 50, 23]


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)


#copying a list
thislist = ["apple", "banana", "cherry"]    
# Using the copy() method
newlist = thislist.copy()  # Creates a shallow copy of the list
print(newlist)  # Output: ['apple', 'banana', 'cherry']
# Using the list() constructor
newlist = list(thislist)  # Creates a shallow copy of the list
print(newlist)  # Output: ['apple', 'banana', 'cherry']
# Using slicing
newlist = thislist[:]  # Creates a shallow copy of the list using slicing   
print(newlist)  # Output: ['apple', 'banana', 'cherry']


# Joining lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)