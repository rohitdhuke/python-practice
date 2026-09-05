# for val in "string":
#     if val == "i":
#         continue
# print(val)
# print("The end")
# n=2
# if n==2:
#     print("executed")
# else:
#     pass

# n=int(input("enter number"))
# row = 1
# while (row<=n):
#     col = 1
#     while (col<=row):
#         col=col+1
#         print("*", end="")
#     print()
#     row = row + 1

x = int(input("enter the number"))

row = x
while row >= 1:
    col = 1
    while col <= row:
        print("*", end="")
        col = col + 1
    print()
    row = row - 1



