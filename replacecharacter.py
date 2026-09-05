def replace(string,char1,char2):
    newstring=''
    for char in string:
        if (char==char1):
            newstring=newstring+char2
        else:
            newstring=newstring+char
    return newstring

string='abcadkbdaxananca'
string=replace(string,'a','R')
print(string)