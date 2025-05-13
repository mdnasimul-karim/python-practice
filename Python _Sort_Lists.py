# Sort Lists

# Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# Customize Sort Function

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# Case Insensitive Sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



# Python - Copy Lists

# Copy a List

# Use the copy() method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# Use the list() method

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# Use the slice Operator

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# Python - Join Lists

# Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# Append list2 into list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print (list1)

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print (list1)


# Python - List Methods

# List Methods

"""
Method	      Description
clear()	      Removes all the elements from the list
append()	    Adds an element at the end of the list
copy()	      Returns a copy of the list
count() 	    Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	      Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()   	    Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	      Sorts the list 
"""