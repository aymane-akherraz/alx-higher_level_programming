#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDg = abs(number) % 10
if number < 0:
    lastDg = -lastDg
print(f"Last digit of {number:d} is {lastDg:d} and is ", end="")
if lastDg > 5:
    print("greater than 5")
elif lastDg == 0:
    print("0")
else:
    print("less than 6 and not 0")
