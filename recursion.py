# def greet():
#     print("Hello")
#     greet()       # function calls itself
#
# greet()
# def n_to_one(n):
#     if n == 0: #base case
#         return
#     print(n)
#     n_to_one(n-1) #recursive call
# n_to_one(5)
#Write a Python program using recursion to print numbers from 1 to n without using a for or while loop.
# def n_to_one(n):
#     if n == 0:
#         return
#     print(n)
#     n_to_one(n-1)
# n_to_one(7)

#Write a recursive function named one_to_n(n) that prints numbers from 1 to n without using any loop.

def one_to_n(n):
    if n == 0:
        return
    one_to_n(n-1)
    print(n)
one_to_n(5)
