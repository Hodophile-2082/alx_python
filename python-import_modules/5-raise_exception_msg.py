class NameException(Exception):
    pass

def raise_exception_msg(message=""):
    if message:
        raise NameException(message)
    else:
        raise NameException("A NameException occurred")

try:
    raise_exception_msg("This is a custom NameException with a message")
except NameException as e:
    print(f"Caught a NameException: {e}")

try:
    raise_exception_msg()
except NameException as e:
    print(f"Caught a NameException: {e}")
