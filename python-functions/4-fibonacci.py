def fibonacci_sequence(n):
    """Returns a list of the first n Fibonacci numbers."""
    fibonacci = [0,1]
    for i in range (2,n):
      fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return fibonacci
  