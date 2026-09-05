# i=0
# j=25
# sum=0
# while i<=j:
#     #if i % 2==0:
#     sum=sum+i
#
#     i = i + 2
# print(sum)

n=int(input("Enter a number: "))
i=2
while i<n:
    isprime=True
    if i%2==0:
        isprime=False
        # print(i)
    else:
        isprime=True
        print(i)
    i=i+1
