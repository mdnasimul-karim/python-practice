""" 
   1) Example: Print numbers from 1 to 10
   and classify them as even or odd using 
   a while loop with if-elif statement
 """
number = 1

while number <= 10:
    if number % 2 == 0:
        print(f"{number} is even")
    elif number % 2 != 0:
        print(f"{number} is odd")
    number += 1


""" 2) Example: Print numbers from 1 to 5, 
skipping even numbers using a 
while loop with continue statement """


number = 0

while number < 5:
    number += 1
    if number % 2 == 0:
        continue
    print(number)


""" 3) Example: Print numbers from 1 to 10 
and classify them as even or odd using 
a for loop with if-elif statement """

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")