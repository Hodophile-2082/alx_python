def raise_exception():
    try:
        raise TypeError("This is a custom TypeError exception")
    except TypeError as e:
        print("Exception raised")
