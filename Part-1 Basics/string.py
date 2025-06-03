# 'hello' is the same as "hello"
print("He is called 'Johnny'")
print('He is called "Johnny"')
a = "Hello"
print(a)
print(len(a))

# multiline strings
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)


for x in "banana":
    print(x, end="")

b = "Hello, World!"
print(b[2:5])

#negative indexing
b = "Hello, World!"
print(b[-5:-2])  #output: "orl"

a = "Hello, World!"
print(a)
a= a.lower()  #convert to lowercase
print(a)

#remove whitespace
a = " Hello, World! "
print(a.strip())  #output: "Hello, World!"

#replace string
a = "Hello, World!"
print(a.replace("World", "Python"))  #output: "Hello, Python!"
#split string
a = "Hello, World!"
print(a.split(","))  #output: ['Hello', ' World!']

#Formatted strings
# Using format() method
name = "Alice"  
place = "Wonderland"
Fstring = "Hello, {}. Welcome to {}!"
formatted_string = Fstring.format(name, place)
print(formatted_string)  #output: "Hello, Alice. Welcome to Wonderland!"

# Using f-strings (Python 3.6+)
name = "subrat"  
place = "Autozone"
Fstring = f"Hello, {name:>10}. Welcome to {place}!"
print(Fstring)  #output: "Hello, subrat. Welcome to Autozone!"

# Escape characters
txt = "We are the so-called \"Vikings\" from the north."

txt = "Helloo00\rWorld!" # Carriage return example
print(txt) 

txt = "Hello \bWorld!" # Backspace example
print(txt) 

ordinal_value = ord('A')  # Get the Unicode code point of 'A'
print(ordinal_value)  # Output: 65
chr_value = chr(65)  # Get the character for Unicode code point 65

print(hex(65))  # Output: '0x41' (hexadecimal representation)
print(bin(65))  # Output: '0b1000001' (binary representation)   
print(oct(65))  # Output: '0o101' (octal representation)


print(x := 3)  # Using the walrus operator to assign and print in one line

# python identity operators
a = "Hello"
b = "Hello"     
print(a is b)  # True, because both variables point to the same string object
c = a   
print(a is c)  # True, because c is assigned to a
print(a is not b)  # False, because a and b point to the same object

# Python membership operators
my_string = "Hello, World!" 
print("Hello" in my_string)  # True, because "Hello" is a substring of my_string
print("Python" not in my_string)  # True, because "Python" is not a substring of my_string