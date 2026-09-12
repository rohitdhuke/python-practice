# def fact(n):
#     if n == 0:
#         return 1
#
#     # print(f'While winding, value of n: {n}')
#
#     small = fact(n - 1)
#
#     # print(f'While unwinding, value of n: {n}')
#     # print('Value returned into small:', small)
#
#     ans = n * small
#     print('Value of ans:', ans)
#
#     return ans
#
# print(fact(5))

def practice(n):
    if n==0:
        return 1
    print(n)
    small_ele=practice(n)
print(practice(5))