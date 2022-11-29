#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number > 0:
    print(f"Last digit of {number} is {int(repr(number)[-1])} ", end="")
    if  int(repr(number)[-1]) > 5:
        print(f"and is greater than 5")
    elif  int(repr(number)[-1]) <= 5 and  int(repr(number)[-1]) > 0:
        print(f"and is less than 6 and not 0")
    elif  int(repr(number)[-1]) == 0:
        print(f"and is 0")
elif number < 0:
    if  int(repr(number)[-1]) == 0:
        print(f"Last digit of {number} is {int(repr(number)[-1])} ", end="")
    else:
        print(f"Last digit of {number} is -{int(repr(number)[-1])} ", end="")
    if  int(repr(number)[-1]) != 0:
        print(f"and is less than 6 and not 0")
    elif  int(repr(number)[-1]) == 0:
        print(f"and is 0")
elif number == 0:
    print(f"Last digit of 0 is 0 and is 0")
else:
    print(f"TypeError")
