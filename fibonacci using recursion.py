def fibonacci(n):
    # Base case:
    # 1st Fibonacci number = 1
    # 2nd Fibonacci number = 1
    if n == 1 or n == 2:
        return 1
    # Recursive call to find the previous Fibonacci number
    fib_1 = fibonacci(n - 1)
    # Recursive call to find the second previous Fibonacci number
    fib_2 = fibonacci(n - 2)
    # Add both previous Fibonacci numbers
    ans = fib_1 + fib_2
    # Return the calculated Fibonacci number
    return ans
# Find the 5th Fibonacci number
print(fibonacci(5))