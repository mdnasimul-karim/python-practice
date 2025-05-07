# Python Operators

print(10 + 5)

# Python Arithmetic Operators

# Addition
x =  167
y = 89

print (x + y)

# Subtraction
x =  167
y = 89

print (x - y)\

# Multiplication
x =  167
y = 89

print (x * y)

# Division
x =  167
y = 89

print (x / y)

# Modulus
x =  167
y = 89

print (x % y)

# Exponentiation
x =  167
y = 89

print (x ** y)

# Floor division
x =  167
y = 89

print (x // y)


# Python Assignment Operators

x = 5

print(x)

# Operator	Example	            Same As	
# =	        x = 5	            x = 5	
# +=	        x += 3	            x = x + 3	
# -=	        x -= 3	            x = x - 3	
# *=	        x *= 3	            x = x * 3	
# /=	        x /= 3	            x = x / 3	
# %=	        x %= 3	            x = x % 3	
# //=	        x //= 3	            x = x // 3	
# **=	        x **= 3	            x = x ** 3	
# &=	        x &= 3	            x = x & 3	
# |=	        x |= 3	            x = x | 3	
# ^=	        x ^= 3	            x = x ^ 3	
# >>=	        x >>= 3	            x = x >> 3	
# <<=	        x <<= 3	            x = x << 3	
# :=	        print(x := 3)	    x = 3
#                                 print(x)



# Python Comparison Operators
""" 
Operator	Name	                    Example	
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y

 """

# Python Logical Operators
""" 
Operator	Description	                                                Example	
and 	    Returns True if both statements are true	                x < 5 and  x < 10	
or	        Returns True if one of the statements is true	            x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)
 """



# And Operators

x = 10

print(x < 3 and x >= 10)

# Or operators:

x = 5

print(x < 3 or x > 10)


# Not operators:
x = 5

print(not(x <= 3 and x >= 10))

x = 5

print(not(x > 3 and x < 10))

# Python Identity Operators
""" 
Operator	Description	                                            Example	
is 	        Returns True if both variables are the same object	    x is y	
is not	    Returns True if both variables are not the same object	x is not y
 """

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# Python Membership Operators
""" 
Operator	Description	                                                                        Example	
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y	
 """
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


# Python Bitwise Operators
""" 
Operator	Name	                Description	                                                                                                Example	
& 	        AND	                    Sets each bit to 1 if both bits are 1	                                                                    x & y	
|	        OR	                    Sets each bit to 1 if one of two bits is 1	                                                                x | y	
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1	                                                            x ^ y	
~	        NOT	                    Inverts all the bits	                                                                                    ~x	
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2	
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2
 """

print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""


print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


# Operator Precedence

print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

print(100 + 5 * 3)

print(5 + 4 - 7 + 3)

""" 
Operator	                                    Description	
()	                                            Parentheses	
**	                                            Exponentiation	
+x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
*  /  //  %	                                    Multiplication, division, floor division, and modulus	
+  -	                                        Addition and subtraction	
<<  >>	                                        Bitwise left and right shifts	
&	                                            Bitwise AND	
^	                                            Bitwise XOR	
|	                                            Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	                                            Logical NOT	
and	                                            AND	
or	                                            OR
 """


