# def greet():
#     print("Hello")
#     greet()       # function calls itself
#
# greet()
def print_num(n):

    if n == 0:       # Base case
        return

    print(n)

    print_num(n - 1) # Recursive call


print_num(3)