#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_number = abs(number) % 10
if number < 0:
    last_digit_number = -last_digit_number
    print("Last digit of {1} is {0} and is ".format(last_digit_number, number), end="")
    if last_digit_number > 5:
        print("greater than 5")
    elif last_digit_number == 0:
        print("0")
    else:
        print("less than 6 and not 0")
