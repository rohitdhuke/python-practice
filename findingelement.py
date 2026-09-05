# li=[1,2,3,4,5,6,7,8,9]
# n=int(input('enter element you want to find: '))
#
# for i in range (len(li)):
#     if n==li[i]:
#         print(i)
#         break
# else:
#     print(-1)
li=[1,2,3,4,5,6,7,8,9]
def linear_search(li,ele):
    for i in range(len(li)):
        if ele == li[i]:
            return i
    return -1
ele=int(input("enter element"))
index=linear_search(li,ele)
print(index)
