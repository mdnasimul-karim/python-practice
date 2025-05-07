myVariableName = "Nasimul"
print(myVariableName)

x,y,z=1,2,3
a=b=c=6
arr=[1,2,3,4,5]
print(b,x,y,z)



# Global Variables

g = "awesome"

def myfunc():
  global  h
  h= "local variable"
  print("Python is " + g)
  #print(h)

myfunc()

print(h)

r=float(5)
print(r)

# p = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(p)

str = "welcome"

print(str[0:4])

