# Python Tuples

# mytuple = ("apple", "banana", "cherry")

# Tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)


# Tuple Items

# Ordered

# Unchangeable

# Allow Duplicates

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)


# type()

# <class 'tuple'>

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

""" 
Python Collections (Arrays)

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
 """

# Python - Access Tuple Items

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


# Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



#   Python - Update Tuples

# Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Add Items
# Convert into a list:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print (thistuple)


# Add tuple to a tuple.:

thistuple = ("apple", "banana", "cherry")
y = ("orange", )

thistuple += y
print (thistuple)

""" 
Note: When creating a tuple with only one item, 
remember to include a comma after the item, 
otherwise it will not be identified as a tuple.
 """

# Remove Items
# Note: You cannot remove items in a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

""" 
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
 """


# Python - Unpack Tuples

# Unpacking a Tuple

# Packing a tuple:

fruits = ("apple", "banana", "cherry")
print (fruits)


# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

""" 
Note: The number of variables must match the number of values in the tuple,
if not, you must use an asterisk to collect the remaining values as a list. 
"""


# Using Asterisk*

# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Python - Loop Tuples  

# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#   Loop Through the Index Numbers


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# Using a While Loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# Python - Join Tuples

# Join Two Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)