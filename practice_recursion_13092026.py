# # Write a recursive function that prints numbers from 1 to N.
# from logging import fatal
#
#
# def print_1_n(n):
#     if n == 0:
#         return
#      print_1_n(n - 1)
#     print(n)
#
# print_1_n(5)
#
# #Factorial
#
# def fact(n):
#     if n == 0:
#         return 1
#     small_ele=fact(n-1)
#     ans = small_ele * n
#     return ans
# fact(5)
#
#Sum of 1 to N using recursion
# def sum_n(n):
#     if n == 0:
#         return 0
#     small_ele = sum_n(n-1)
#     ans=small_ele + n
#     return ans
# print(sum_n(10))

# UNWINDING ↑
#
# sum_n(1): small_ele = 0  → ans = 0 + 1  = 1
# sum_n(2): small_ele = 1  → ans = 1 + 2  = 3
# sum_n(3): small_ele = 3  → ans = 3 + 3  = 6
# ...
# sum_n(10): small_ele = 45 → ans = 45 + 10 = 55

#Power

# def power(x, n):
#
#     # Base case:
#     # Any non-zero number raised to power 0 is 1
#     if n == 0:
#         return 1
#
#     # WINDING:
#     # Reduce the power by 1 and solve the smaller problem
#     # Example: power(2, 3) waits for power(2, 2)
#     small_ele = power(x, n - 1)
#
#     # UNWINDING:
#     # small_ele contains the answer returned by the smaller call
#     # Multiply x by that previous returned answer
#     # Example: if small_ele = 4, then 2 * 4 = 8
#     ans = x * small_ele
#
#     # Return the current answer.
#     # This ans becomes small_ele for the next waiting call
#     return ans
#
#
# print(power(2, 3))

#
# Winding   → n decreases: 3 → 2 → 1 → 0
#
# Base case → returns 1 and starts unwinding
#
# Unwinding → x × previous returned answer
#
# return ans → becomes small_ele of the next waiting call

#count the digits in numbers


# def count_digits(n):
#
#     # Base case:
#     # When no digits are left, return 0
#     # This 0 starts the first step of unwinding
#     if n == 0:
#         return 0
#
#     # WINDING:
#     # Remove the last digit using // 10
#     # Example: 1234 -> 123 -> 12 -> 1 -> 0
#     small_ele = count_digits(n // 10)
#
#     # UNWINDING:
#     # small_ele contains the number of digits counted so far
#     # Add 1 for the current digit
#     # The returned value becomes small_ele for the next waiting call
#     return small_ele + 1
#
#
# print(count_digits(8669864286))


# Winding:
# 8669864286 → 866986428 → ... → 8 → 0
#
# Base case:
# 0 → return 0
#
# Unwinding:
# 0 + 1 → 1
# 1 + 1 → 2
# 2 + 1 → 3
# ...
# 9 + 1 → 10



