# a= int (input("Enter first number: "))
# b= int (input("Enter second number: "))
# if a==b:
#     c= True
#     print(f"Vaules of two no is {c}")
# else:
#     c= False
#     print(f"Vaules of two no is {c}")

# a= int (input("Enter first number: "))
# b= int (input("Enter second number: "))
# x= int (input("Enter third number: "))
# d= int (input("Enter fourth number: "))
# if a==b and ( (a== x) or (a== d)) :
#     # if (a==x or a==d):
#         c= True
#         print(f"Vaules of two no is {c}")
# else:
#     c= False
#     print(f"Vaules of two no is {c}")

# a= int (input("Enter first number: "))
# b= int (input("Enter second number: "))
# c= int (input("Enter third number: "))
# if (a>b and a>c):
#     print(f" {a}>> is greater than b and c ")
# elif (b>a and b>c):
#     print(f"{b}>> is greater than a and c ")
# elif (c>a and c>b):
#     print(f"{c}>> is greater than a and b ")
# else:
#     print("all the valuse are same")


a = int(input("enter value one : "))
b = int(input("enter value two : "))
c = int(input("enter value three : "))
if (a > b) and (a > c):
    print(f"{a} a is greater then b,c")
elif (b > a) and (b > c):
    print(f"b is highest {b}")
elif (c > a) and (c > b):
    print(f"c is highest {c}")
elif (a == b == c):
    print("all the values are same")
else:
    if (a == b):
        if (a < c):
            print("c is highest and a and b is same")
        else:
            print("a and b are equal and greater then c")
    elif (a == c):
        if (a < b):
            print("b is highest and a and c is same")
        else:
            print("a and c are equal and greater then b")
    elif (b == c):
        if (b < a):
            print("a is highest and b and c is same")
        else:
             print("b and c are equal and greater then a")



