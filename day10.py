list1=[1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
# 1. Finding first occurrence of the given number.
# 2. Finding the last occurrence of the given number.
l=len(list1)
fst=int(input("enter the number first occurence"))

for i in range(l):
    if list1[i]==fst:
        print(list1.index(i))
        break
else:
    print("not found")

for j in range ((l)-1,-1,-1):
    if list1[j]==fst :
        print(j)
        break




