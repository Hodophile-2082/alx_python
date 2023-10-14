def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)

    return fibonacci_list[:n]