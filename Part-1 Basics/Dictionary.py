# Dictionary items are ordered, changeable, and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(type(thisdict))  # Output: <class 'dict'>
print(len(thisdict))
print("----")
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# Accessing items
print(thisdict["brand"])  # Output: Ford
print(thisdict.get("model"))  # Output: None (key does not exist)
# Accessing items with a default value
print(thisdict.get("model", "Default Model"))

thisdict["model"] = "Mustang"  # Change the value of an existing key


# print all keys in form of a list
x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

# print all items in form of a list
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)

if "model" in thisdict:
  print("Yes")

#change/add values
thisdict["year"] = 2020  # Change the value of an existing key
print(thisdict)
thisdict.update({"year": 2021})  # Update the value of an existing key
print(thisdict)

#adding items
thisdict["Month"] = "june"  # Add a new key-value pair

#upadting key names
thisdict['modeling'] = thisdict.pop('model')
print(thisdict)  # Output: {'brand': 'Ford', 'year': 2021, 'colors': ['red', 'white', 'blue'], 'Month': 'june', 'modeling': 'Mustang'}

# The pop() method removes the item with the specified key name:
# The popitem() method removes the last inserted item

del thisdict["modeling"]

# thisdict.clear()
# print(thisdict)

print("----")
#loop through a dictionary
for key in thisdict:
    print(key, ":", thisdict[key])  # Output: brand : Ford, year : 2021, colors : ['red', 'white', 'blue'], Month : june
print("----")
# Loop through keys and values
for key, value in thisdict.items():
    print(key, ":", value)  # Output: brand : Ford, year : 2021, colors : ['red', 'white', 'blue'], Month : june
print("----")
# Loop through values
for value in thisdict.values():
    print(value)  # Output: Ford, 2021, ['red', 'white', 'blue'], june

# Copying a dictionary
newdict = thisdict.copy()  # Create a shallow copy of the dictionary
print(newdict)  # Output: {'brand': 'Ford', 'year': 2021, 'colors': ['red', 'white', 'blue'], 'Month': 'june'}

mydict = dict(thisdict)
print(mydict)

print("----")

# Nested dictionaries
nested_dict = {
    "car": {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    "owner": {
        "name": "John",
        "age": 30
    }
}
print(nested_dict)
# Accessing nested dictionary items
print(nested_dict["car"]["brand"])  # Output: Ford
print(nested_dict["owner"]["name"])  # Output: John
# Adding a new nested dictionary
nested_dict["location"] = {
    "city": "New York",
    "country": "USA"
}
print(nested_dict)
# Accessing nested dictionary items 
print(nested_dict["location"]["city"])  # Output: New York
# Looping through a nested dictionary
for key, value in nested_dict.items():
    print(key, ":", value)

