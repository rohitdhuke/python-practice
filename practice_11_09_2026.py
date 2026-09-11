# ============================================================
# PYTHON RECURSION PRACTICE
# Date: 11-09-2026
# ============================================================


# ============================================================
# QUESTION 1: Factorial of a Number Using Recursion
#
# Example:
# 5! = 5 * 4 * 3 * 2 * 1
# Output: 120
# ============================================================

def factorial(n):

    # Base case:
    # 0! is always 1
    if n == 0:
        return 1

    # Recursive call:
    # Find factorial of the smaller number
    small_output = factorial(n - 1)

    # Multiply current number with factorial of smaller number
    ans = n * small_output

    return ans


print("Factorial of 5:", factorial(998))


# ============================================================
# QUESTION 2: Sum of First N Natural Numbers Using Recursion
#
# Example:
# 1 + 2 + 3 + 4 + 5 = 15
# ============================================================

# def sum_n(n):
#
#     # Base case:
#     # Sum up to 0 is 0
#     if n == 0:
#         return 0
#
#     # Recursive call:
#     # Find sum up to n - 1
#     small_output = sum_n(n - 1)
#
#     # Add current number
#     total = small_output + n
#
#     return total
#
#
# print("Sum of first 10 numbers:", sum_n(10))
#
#
# # ============================================================
# # QUESTION 3: Calculate Power Using Recursion
# #
# # Example:
# # 2^5 = 2 * 2 * 2 * 2 * 2
# # Output: 32
# # ============================================================
#
# def power(x, n):
#
#     # Base case:
#     # Any number raised to power 0 is 1
#     if n == 0:
#         return 1
#
#     # Recursive call:
#     # Calculate x^(n-1)
#     small_output = power(x, n - 1)
#
#     # Multiply x with the smaller answer
#     ans = x * small_output
#
#     return ans
#
#
# print("2 power 5:", power(2, 5))
#
#
# # ============================================================
# # QUESTION 4: Count Digits Using Recursion
# #
# # Example:
# # Number: 12345
# # Output: 5
# #
# # n // 10 removes the last digit:
# # 12345 -> 1234 -> 123 -> 12 -> 1 -> 0
# # ============================================================
#
# def count_digits(n):
#
#     # Base case:
#     # When n becomes 0, there are no more digits to count
#     if n == 0:
#         return 0
#
#     # Recursive call:
#     # Remove the last digit
#     small_output = count_digits(n // 10)
#
#     # Count the digit that was removed
#     ans = small_output + 1
#
#     return ans
#
#
# print("Number of digits in 12345:", count_digits(12345))