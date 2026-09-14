

def replace_pi(string):
    if len(string) <= 1:
        return string
    if string[0]=='p' and string[1]=='i':
        small_letter = replace_pi(string[2:])
        return '3.14' + small_letter
    else:
        small_letter =replace_pi(string[1:])
        return string[0]+ small_letter

string='xpix'
print(replace_pi(string))

