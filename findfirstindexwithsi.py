def first_index(arr,x,si):
    if si == len(arr):
        return -1
    if arr[si] == x:
        return si
    small_ele=first_index(arr,x,si+1)
    return small_ele

arr=[10,20,30,40,10]
print(first_index(arr,30,0))


# si = 0 → arr[0] = 10 → not 30
#                          ↓
# si = 1 → arr[1] = 20 → not 30
#                          ↓
# si = 2 → arr[2] = 30 → FOUND
#                          ↓
#                       return 2
#                          ↑
#               small_ele = 2
#               return 2
#                          ↑
#               small_ele = 2
#               return 2
#
# Final answer = 2

