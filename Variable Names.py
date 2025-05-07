myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MyVar = "John"
myvar2 = "John"



#2myvar = "John"
#my-var = "John"
#my var = "John"


#Multi Words Variable Names

#Camel Case

myVaribleName = "John"

#Pascal Case

MyVariableName = "John"

#Snake Case

my_variable_name = "John"


# Assign Multiple Values

# Many Values to Multiple Variables  


a, b ,c = "Apple", "Orange", "Banana"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# One Value to Multiple Variables

a = b = c = "Hello World"

x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection

fruits =["Apple", "Banana", "Cherry"]
x, y, z = fruits
print (x)
print (y)
print (z)


# Output Variables


x = "Python is awesome"
print(x)



x = "Python"
y = "is"
z = "awesome"
print(x, y, z)



x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

"""
x = 5
y = "John"
print(x + y)
"""


x = 5
y = "John"
print(x, y)


#Global Variables


x = " awesome"

def myfunc ():
    print ("Python is" + x)
    
myfunc()


x = " awesome"

def myfunc ():
 x = " fantastic"   
 print ("Python is" + x)
    
myfunc()
print ("Python is" + x)


# The global Keyword

def myfunc ():
 global x
x = " fantastic"   
  
myfunc()

print ("Python is" + x)

x = " awesome"

def myfunc ():
 global x
 x = " fantastic"   
 

myfunc()
print ("Python is" + x)


