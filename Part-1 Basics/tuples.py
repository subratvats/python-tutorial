# ordered and unchangeable

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# create a tuple with one item
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# tuple constructor
tuple2 = tuple(("apple", "banana", "cherry"))
print(tuple2)  # Output: ('apple', 'banana', 'cherry')

# updating tuples
# Tuples are immutable, so you cannot change their items.
# However, you can convert a tuple to a list, change the list, and convert it back to a tuple.
# Example of converting a tuple to a list, modifying it, and converting it back to a tuple
tuple3 = ("apple", "banana", "cherry")
list_from_tuple = list(tuple3)  # Convert tuple to list
list_from_tuple[1] = "blackcurrant"  # Change the second item
tuple3 = tuple(list_from_tuple)  # Convert list back to tuple
print(tuple3)  # Output: ('apple', 'blackcurrant', 'cherry')

#add tuple to a tuple
tuple4 = ("apple", "banana", "cherry")  
tuple5 = ("orange", "kiwi", "melon")
tuple4 += tuple5  # Concatenate tuples  
print(tuple4)  # Output: ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon')

#packing and unpacking tuples
# Packing a tuple
packed_tuple = ("apple", "banana", "cherry")  # Tuple packing
# Unpacking a tuple
a, b, c = packed_tuple  # Tuple unpacking
print(a)  # Output: 'apple'
print(b)  # Output: 'banana'
print(c)  # Output: 'cherry'

# if no of variables is less than the no of items in tuple
# Unpacking with an asterisk    
a, *b = packed_tuple  # 'a' gets the first item, 'b' gets the rest
print(a)  # Output: 'apple' 
print(b)  # Output: ['banana', 'cherry']