def add(a, b):
    return a + b

if __name__ == "__main__":
    x = 5
    y = 10
    result = add(x, y)
    message = "The sum of {} and {} is {}".format(x, y, result)
else:
    message = "0-add.py doesn't contain: ['__name__']"

print(message)