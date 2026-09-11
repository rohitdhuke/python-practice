
# ============================================================
# RECURSION PRACTICE
# ============================================================


# 1. Sum of First N Natural Numbers
# Example: 1 + 2 + 3 + 4 + 5 = 15

def sum_n(n):
    # Base case
    if n == 0:
        return 0

    # Calculate sum of smaller problem
    small_op = sum_n(n - 1)

    # Add current number
    ans = small_op + n

    return ans


print("Sum:", sum_n(5))


# ------------------------------------------------------------


# 2. Multiply Numbers From 1 to N
# Example: 1 * 2 * 3 * 4 = 24

def multiply_n(n):
    # Base case
    if n == 0:
        return 1

    # Calculate smaller problem
    small_out = multiply_n(n - 1)

    # Multiply current number
    mul = small_out * n

    return mul


print("Multiplication:", multiply_n(4))


# ------------------------------------------------------------


# 3. Print Numbers From N to 1
# Example: 5 4 3 2 1

def print_n_to_1(n):
    # Base case
    if n == 0:
        return

    # Print before recursive call
    print(n)

    # Recursive call
    print_n_to_1(n - 1)


print("\nN to 1:")
print_n_to_1(5)


# ------------------------------------------------------------


# 4. Print Numbers From 1 to N
# Example: 1 2 3 4 5

def print_1_to_n(n):
    # Base case
    if n == 0:
        return

    # Recursive call
    print_1_to_n(n - 1)

    # Print while recursion is returning
    print(n)


print("\n1 to N:")
print_1_to_n(5)


# ------------------------------------------------------------


# 5. Print While Going Down and Coming Up
# For n = 3:
# Output: 3 2 1 1 2 3

def fun(n):
    # Base case
    if n == 0:
        return

    # Print while going down
    print(n)

    # Recursive call
    fun(n - 1)

    # Print while coming back up
    print(n)


print("\nDown and Up:")
fun(3)


# ------------------------------------------------------------


# 6. Power of a Number
# Example: 2^4 = 16

def power(x, n):
    # Base case
    if n == 0:
        return 1

    # Calculate x^(n-1)
    small_out = power(x, n - 1)

    # Multiply by current x
    ans = x * small_out

    return ans


print("\nPower:", power(2, 4))


# ------------------------------------------------------------


# 7. Count Digits
# Example: 12345 has 5 digits

def count_digits(n):
    # Base case
    if n == 0:
        return 0

    # Remove the last digit
    small_out = count_digits(n // 10)

    # Count the current digit
    ans = small_out + 1

    return ans


print("\nNumber of digits:", count_digits(12345))
