#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#This ensures that the last digit is always positive
last_digit = abs(number) % 10
#initialize condition to an empty string
condition = " "
if last_digit > 5:
    condition = " and is greater than 5"
elif last_digit == 0:
    condition = " and is 0"
else:
    condition = " and is less than 6 and not 0"

#print the output
print("Last number {} is {} {}".format(number, last_digit, condition))
