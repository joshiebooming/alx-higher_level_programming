#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_m = ("Last digit of")
if number < 0:
    last = number % -10
elif number >= 0:
    last = number % 10
if last > 5:
    print("{} {} is {} and is greater than 5".format(l_m, number, last))
elif last == 0:
    print("{} {} is {} and is 0".format(l_m, number, last))
else:
    print("{} {} is {} and is less than 6 and not 0".format(l_m, number, last))
