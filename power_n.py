# Write a program to find x to the power n
#
# Note : For this question, you can assume that 0 raised to the power of 0 is 1

def power_n(x,n):
    if n==0:
        return 1
    small_ele=power_n(x,n-1)
    x= x * small_ele
    return x

print(power_n(2,5))
