def sum_digits(n):

    # Base case:
    # When no number/digits are left, return 0.
    # This 0 starts the first step of unwinding.
    if n == 0:
        return 0

    # WINDING:
    # Remove the last digit using // 10.
    # Each recursive call has its own value of n stored in the call stack.
    # Example:
    # 1234 -> 123 -> 12 -> 1 -> 0
    small_ele = sum_digits(n // 10)

    # UNWINDING:
    # The stored values of n come back one by one in reverse order.
    # n % 10 gives the current digit of that call.
    # small_ele contains the sum calculated so far.
    #
    # Example:
    # n = 1   -> small_ele = 0 -> 0 + 1 = 1
    # n = 12  -> small_ele = 1 -> 1 + 2 = 3
    # n = 123 -> small_ele = 3 -> 3 + 3 = 6
    ans = small_ele + (n % 10)

    # Return the current sum.
    # This ans becomes small_ele for the next waiting call.
    return ans


print(sum_digits(8669864286))
#
# Winding   → each call keeps its own n
# Unwinding → those n values resume one by one
# n % 10    → gets the current digit
# small_ele → carries the sum calculated so far