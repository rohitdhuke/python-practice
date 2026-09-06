# a="ascindapur"
# b="ascindapur"
# if id(a)==id(b):
#     print("they are same")
# else:
#     print("they are different")
# a='arts,science'
# b='arts,science'
# print (id(a),id(b))
# #     print("they are same")
# # else:
# #     print("they are different")
# li=['suraj','javir']
# li.insert(1,'ramchandra')
# print(li)

# c=a+b
# print(c)
#
# print(len("malayalam"))
#check the string is palindrome or not
# n=input('enter a string ')
# i=0
# j=len(n)-1
# a=True
# while i<j:
#     if n[i]==n[j]:
#         i+=1
#         j-=1
#     else:
#         a=False
#         break
# if a:
#     print(f' {n} is palindrome')
# else:
#     print(f' {n} is not palindrome')
# Take a string as input from the user
string = input("Enter string: ")

# Empty string to store only letters/numbers in lowercase
newstring = ''

# Initially assume that the string is a palindrome
a = True


# Loop through every character of the original string
for ch in string:

    # Check whether the character is a letter or number
    # Spaces and special characters will be ignored
    if ch.isalnum():

        # Convert character to lowercase and add it to newstring
        newstring += ch.lower()


# i starts from the first character
i = 0

# j starts from the last character
j = len(newstring) - 1


# Continue checking until i and j meet in the middle
while i < j:

    # Compare character from the beginning with character from the end
    if newstring[i] == newstring[j]:

        # Move i one position forward
        i += 1

        # Move j one position backward
        j -= 1

    else:
        # If characters don't match, it is not a palindrome
        a = False

        # No need to check remaining characters
        break


# Check the final result
if a:
    print('Palindrome')
else:
    print('Not palindrome')






