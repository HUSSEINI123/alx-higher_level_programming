#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "and is greater than 5"
str2 = "and is 0"
str3 = "and is less than 6 and not 0"
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
if last_digit > 5:
    print("Last digit of {} is {} ".format(number, last_digit) + str1)
elif number % 10 == 0:
    print("Last digit of {} is {} ".format(number, last_digit) + str2)
else:
    print("Last digit of {} is {} ".format(number, last_digit) + str3)
