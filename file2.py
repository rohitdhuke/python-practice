# a = 5.2
# a= "rohit"
# print(type (a))

def fun(n):
    if(n == 4):

        return n

    else:
        ans=2 *fun(n+1)

        return ans



print(fun(2))