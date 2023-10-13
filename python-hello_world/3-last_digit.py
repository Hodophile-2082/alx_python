#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit = abs(number) % 10
greater_than_5 = "greater than 5"
is_0 = "0"
less_than_6 = "less than 6 and not 0"

if number < 0:
    last_digit *= -1

print("The string Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is", greater_than_5)
elif last_digit == 0:
    print("and is", is_0)
else:
    print("and is", less_than_6)





