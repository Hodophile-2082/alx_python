#!/usr/bin/python3
def add(a, b):
    return a + b

from add_0 import add
if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    message = "{} + {} = {}".format(a, b, result)
else:
    message = "0-add.py doesn't contain: ['__name__']"

print(message)