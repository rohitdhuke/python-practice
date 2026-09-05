# userinput=input("enter the number")
# mylist=[int(x) for x in userinput.split() ]
# mylist2 = sorted(mylist)
# print(mylist2)
# mylist=[range(1,101,2)]
# print(mylist)
b=0
a=int(input("enter number"))
    # b=int(input("enter number"))
    # c=int(input("enter number"))
for i in range(2,a):
    if (a%2==0):
        #print("i")
        b=1
if (b==0):
    print("prime")
else:
    print("not prime")
