#set is a collection which is unordered, unchangeable*, and unindexed.
myset = {"apple", "banana", "cherry"}
print(myset)  # Output: {'banana', 'cherry', 'apple'}

# Note: The order of elements in a set may vary, as sets are unordered.

# set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)  # Output: apple banana cherry (order may vary)


# change items in a set
# Once a set is created, you cannot change its items, 
# but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")  # Add an item
print(thisset)  # Output: {'banana', 'cherry', 'orange', 'apple'}   

# Add multiple items using update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#remove items in a set
thisset = {"apple", "banana", "cherry"} 
thisset.remove("banana")  # Remove "banana"
print(thisset)  # Output: {'cherry', 'apple'}
# Note: If the item to be removed does not exist, remove() will raise an error.
# Remove an item using discard()
thisset = {"apple", "banana", "cherry"} 
thisset.discard("banana")  # Remove "banana"
print(thisset)  # Output: {'cherry', 'apple'}
# Note: If the item to be removed does not exist, discard() will not raise an error.
# Remove an item using pop()
thisset = {"apple", "banana", "cherry"}
popped_item = thisset.pop()  # Remove and return an arbitrary item
print(popped_item)  # Output: 'apple' (or another item, as sets are unordered)
print(thisset)  # Output: {'banana', 'cherry'} (the popped item is removed)

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#joining sets
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "kiwi", "melon"}
set3 = set1.union(set2)  # Join two sets
print(set3)  # Output: {'banana', 'kiwi', 'melon', 'orange', 'cherry', 'apple'} 
# Note: The union() method returns a new set that contains all items from both sets.
# You can also use the '|' operator to join sets    
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "kiwi", "melon"}  
set3 = set1 | set2  # Join two sets using the '|' operator
print(set3)  # Output: {'banana', 'kiwi', 'melon', 'orange', 'cherry', 'apple'}
# Repeating sets
set1 = {"apple", "banana", "cherry"}
set2 = set1.copy()  # Create a copy of set1
set3 = set1 | set2  # Join set1 with its copy
print(set3)  # Output: {'banana', 'cherry', 'apple'} (no duplicates in sets)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)