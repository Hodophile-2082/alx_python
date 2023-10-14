def is_prime(number):
  if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    return False
  else:
    return True
