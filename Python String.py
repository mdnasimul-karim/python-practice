""" price = 59
txt = f"The price is\n {price:.2f} dollars"
print(txt) """

#Strings

print("Hello")
print('Hello')

# Quotes Inside Quotes

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable

a = "Hello"
print(a)

# Multiline Strings
# Example
# use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a ="\n"
print (a)
# Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# Python - Slicing Strings

# Slicing

b = "Hello, World!"
print (b [2:5])

# Note: The first character has index 0.

# Slice From the Start

b = "Hello, World!"
print (b [:5])

# Slice To the End

b = "Hello, World!"
print (b [2:])


# Negative Indexing

b = "Hello, World!"
print (b [-5:-2])


# Python - Modify Strings

# Upper Case

a = "Hello, World!"
print(a.upper())

# Lower Case

a = "Hello, World!"
print(a.lower())

# Remove Whitespace

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# Python - String Concatenation

# String Concatenation

a = "Hello"
b = "World"
c = (a +  b)
print(c)


# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


# Python - Format - Strings

# String Format

""" age = 36
txt = "My name is John, I am " + age
print(txt) """

# F-Strings

age = 36
txt = f"My name is John, I am  {age}"
print(txt)

# Placeholders and Modifiers

Price = 59
txt = f"The price is {Price} dollars"
print(txt)

# Display the price with 2 decimals:

Price = 59
txt = f"The price is {Price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20*59} dollars"
print(txt)


# Python - Escape Characters

# Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Escape Characters

# Other escape characters used in Python:


# Code	Result	
# \'	    Single Quote	
# \\	    Backslash	
# \n	    New Line	
# \r	    Carriage Return	
# \t	    Tab	
# \b	    Backspace	
# \f	    Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x61\x6c\x61\x6c"
print(txt) 

# Python - String Methods

# String Methods

# Note: All string methods return new values. They do not change the original string.

""" Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning """