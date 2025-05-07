

# Python Lists

# List

mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

# Allow Duplicates

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# List Length

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


list1 = ["abc", 34, True, 40, "male"]

print(list1)

# type()

mylist = ["apple", "banana", "cherry"]

print(type(mylist))


# The list() Constructor

thislist = list(("apple", "banana", "cherry"))
 # note the double round-brackets
print(thislist)

# Exercise

thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist)

""" 
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

 """


#  Python - Access List Items

# Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Range of Negative Indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# Python - Change List Items


# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Python - Add List Items

# Append Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Python - Remove List Items

# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



# Python - Loop Lists

# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range (len(thislist)):
  print(thislist[i])


# Using a While Loop


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]