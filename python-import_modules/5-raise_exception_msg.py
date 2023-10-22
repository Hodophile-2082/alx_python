def raise_exception_msg(message="C is fun"):
    if message:
        raise NameException(message)
    else:
        raise NameException("A NameException occurred")

