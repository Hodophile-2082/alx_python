for number in range(100):
    print("{:02}{}".format(number, ', ' if number < 99 else '\n'), end='')