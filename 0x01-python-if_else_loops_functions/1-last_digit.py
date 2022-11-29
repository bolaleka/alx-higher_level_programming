#!/usr/bin/python3
import random

n = random.randint(-10000, 10000)
if n > 0:
    print(f"Last digit of {n} is {int(repr(n)[-1])} ", end="")
    if int(repr(n)[-1]) > 5:
        print("and is greater than 5")
    elif int(repr(n)[-1]) <= 5 and int(repr(n)[-1]) > 0:
        print("and is less than 6 and not 0")
    elif int(repr(n)[-1]) == 0:
        print("and is 0")
elif n < 0:
    if int(repr(n)[-1]) == 0:
        print(f"Last digit of {n} is {int(repr(n)[-1])} ", end="")
    else:
        print(f"Last digit of {n} is -{int(repr(n)[-1])} ", end="")
    if int(repr(n)[-1]) != 0:
        print("and is less than 6 and not 0")
    elif int(repr(n)[-1]) == 0:
        print("and is 0")
elif n == 0:
    print("Last digit of 0 is 0 and is 0")
else:
    print("TypeError")
