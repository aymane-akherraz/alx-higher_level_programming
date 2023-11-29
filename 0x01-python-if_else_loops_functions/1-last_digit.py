#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number:d} is ", end="")
if number < 0:
    number = -number
    last_dg = -(number % 10)
else:
    last_dg = number % 10
print(f"{last_dg:d} ", end="")
if last_dg > 5:
    print("and is greater than 5")
elif last_dg == 0:
    print('and is 0')
elif last_dg < 6 and last_dg:
    print("and is less than 6 and not 0")
