# Given a 2D integer array with n rows and m columns. Print the 0th row from input n times, 1st row n-1 times…..(n-1)th row will be printed 1 time.
#
# Detailed explanation ( Input/output format, Notes, Images )
# Input format :
# Line 1 : No of rows (n) and no of columns (m) (separated by single space)
# Line 2 : Row 1 elements (separated by space)
# Line 3 : Row 2 elements (separated by space)
# Line 4 : and so on
# n,m=map(int,(input().split()))
# li=[]
# for i in range(n):
#     row=list(map(int, input().split()))
#     li.append(row)
# for i in range(n):
#     for j in range(n-i):
#         for k in range (len(li[i])):
#             print(li[i][k],end=" ")
#         print( )

def fun(n):
    if(n == 4):
        return n
    else:
        return 2*fun(n+1)


print(fun(2))