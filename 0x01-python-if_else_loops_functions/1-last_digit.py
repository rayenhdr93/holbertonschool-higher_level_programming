#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    x = -number
else:
    x = number
n = x % 10
if n == 0:
    print("Last digit of {:d} is 0 and is 0".format(number, number % 10))
elif n < 6 or number < 0:
    print(
        "Last digit of {:d} is {:} and is less than 6 and not 0".format(
            number, int((x % 10) * (number / x))))
else:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, n))
