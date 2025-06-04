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