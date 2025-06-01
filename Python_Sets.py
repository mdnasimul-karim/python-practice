
# Python Sets

# myset = {"apple", "banana", "cherry"}

# Set

# * Note: Set items are unchangeable, but you can remove items and add new items.

# Sets are written with curly brackets.

# Example
# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Duplicates Not Allowed

# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)



# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


# Get the Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# Set Items - Data Types

# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)


# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

print(set1)

# type()
# From Python's perspective, sets are defined as objects with the data type 'set':

# <class 'set'>


myset = {"apple", "banana", "cherry"}
print(type(myset))


# The set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)