def remove_consucative(string):
    if len(string) <=1:
        return string

    small_letter=remove_consucative(string[1:])
    if string[0] == string[1]:
        return small_letter
    else:
        small_letter=remove_consucative(string[1:])
        return string[0]+small_letter

string='aabccba'
print(remove_consucative(string))

# If the recursive call is the same for every condition
# → write it once outside the if
# 
# If different conditions need different recursive calls
# → write them inside the respective if/else blocks