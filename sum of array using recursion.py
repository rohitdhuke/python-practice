def sum_arr(arr,):
    if len(arr)==0:
        return 0
    small_ele=sum_arr(arr[1:])
    return arr[0] + small_ele

arr=[10,20,30,40]
print(sum_arr(arr))

#
# Call 1 → arr=[10,20,30,40] → waiting
# Call 2 → arr=[20,30,40]    → waiting
# Call 3 → arr=[30,40]       → waiting
# Call 4 → arr=[40]          → waiting
# Call 5 → arr=[]            → return 0
#
# Unwinding:
# 
# Call 4 → small_ele=0  → 40+0  = 40
# Call 3 → small_ele=40 → 30+40 = 70
# Call 2 → small_ele=70 → 20+70 = 90
# Call 1 → small_ele=90 → 10+90 = 100