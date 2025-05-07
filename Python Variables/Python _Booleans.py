a = 200
b = 33

if b > a:
  print("True")
else:
  print("False")

  
# Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)

# 
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  # Evaluate Values and Variables

  print(bool("Hello"))
  print(bool(15))


  # Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True

# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])

print (bool("abc"))
print (bool(123))
print (bool(["apple", "cherry", "banana"]))

# Some Values are False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def  __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean

def myfunction() :
  return True
print (myfunction())

def myfunction() :
  return True
if myfunction():
  print ("Yes!")
else:
  print("No!")


# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
