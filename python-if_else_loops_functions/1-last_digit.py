#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end= " ")
if number < 0:
    print(f"{abs(number) % 10 * -1}", end= " ")
if number % 10 > 5:
    print( "and is greater than 5")
elif number % 10 == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
