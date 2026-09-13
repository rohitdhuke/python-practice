def reverse_print(n):
    if n == 0:
        return

    # During winding, get and print the last digit
    print(n % 10, end="")

    # Remove the last digit
    reverse_print(n // 10)


reverse_print(1234)