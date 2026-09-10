# a=int(input("enter value"))
# b=int(input("enter power value"))
# ans=1
# while b!=0:
#     ans*=a
#     b-=1
# print(ans)
def fnd_pwr(a,b):
    if b==0:
        return 1
    ans=fnd_pwr(a,(b-1))
    return ans * a

a=int(input())
b=int(input())
print(fnd_pwr(a,b))

