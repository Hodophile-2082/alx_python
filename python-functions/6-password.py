def validate_password(password):
  if len(password) < 8:
    return False

  # Check for uppercase, lowercase, and digit
  has_upper = False
  has_lower = False
  has_digit = False

  for char in password:
    if char.isupper():
      has_upper = True
    elif char.islower():
      has_lower = True
    elif char.isdigit():
      has_digit = True

    if has_upper and has_lower and has_digit:
      break

  else:
    return False

  # Check for spaces
  if ' ' in password:
    return False

  return True
