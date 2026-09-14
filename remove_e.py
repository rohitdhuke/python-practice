def remove_e(string, a, b):
    if len(string) == 0:
        return ''
    small_letter = remove_e(string[1:], a, b)
    if string[0] == a:
        return b + small_letter
    else:
        return string[0] + small_letter


string = 'english'
print(remove_e(string, 'e', 'h'))