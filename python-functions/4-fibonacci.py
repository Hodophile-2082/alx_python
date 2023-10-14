def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_list = []
    a, b = 0, 1

    while len(fibonacci_list) < n:
        fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list

# Example usage:
n = 10  # Replace with the desired number of Fibonacci numbers
result = fibonacci_sequence(n)
print(result)  # This will print the first 10 Fibonacci numbers