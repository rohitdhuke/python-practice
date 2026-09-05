# Read input as sepcified in the question
# Print output as specified in the question
def checkPalindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if not s[i].isalnum():
            i += 1

        elif not s[j].isalnum():
            j -= 1

        elif s[i] != s[j]:
            return False

        else:
            i += 1
            j -= 1

    return True


s = input()

if checkPalindrome(s):
    print("true")
else:
    print("false")
# str='hey i am jarvis'
# str=str.replace('jarvis','friday')
# print(str)
# string = 'hello im jarvis '
# index=string.find('jar')
# print(index)
# str='hello i am jarvis'
# li=str.split()
# print(li)
# str='hEy My naMe iS jaRviS'
# str=str.lower()
# print(str)
# str=str.upper()
# print(str)
str='hEy My naMe iS jaRviS'
str=str.startswith('hEy M')
print(str)
