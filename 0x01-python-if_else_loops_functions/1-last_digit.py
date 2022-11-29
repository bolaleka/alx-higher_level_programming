#!/usr/bin/python3
import random

n = random.randint(-10000, 10000)
if n > 0:
    print(f"Last digit of {n} is {n % 10} ", end="")
    if n % 10 > 5:
        print(f"and is greater than 5")
    elif n % 10 <= 5 and n % 10 > 0:
        print(f"and is less than 6 and not 0")
    elif n % 10 == 0:
        print(f"and is 0")
elif n < 0:
    if n % 10 == 0:
        print(f"Last digit of {n} is {n % 10} ", end="")
    else:
        print(f"Last digit of {n} is -{n % 10} ", end="")
    if n % 10 != 0:
        print(f"and is less than 6 and not 0")
    elif n % 10 == 0:
        print(f"and is 0")
elif n == 0:
    print(f"Last digit of 0 is 0 and is 0")
else:
    print(f"TypeError")
