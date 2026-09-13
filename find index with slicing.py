def find_index(arr, x):
    if len(arr) == 0:
        return -1
    if arr[0] == x:
        return 0
    small_ele=find_index(arr[1:],x)
    if small_ele == -1:
        return -1
    return small_ele + 1

arr=[10,20,30,40,50]
print(find_index(arr,40))

# arr = [10,20,30,40,50], x = 40
#
# [10,20,30,40,50] → arr[0] = 10 → not 40
#                                  ↓
# [20,30,40,50]    → arr[0] = 20 → not 40
#                                  ↓
# [30,40,50]       → arr[0] = 30 → not 40
#                                  ↓
# [40,50]          → arr[0] = 40 → FOUND
#                                  ↓
#                               return 0
#                                  ↑
#                    small_ele = 0
#                    return 0 + 1 = 1
#                                  ↑
#                    small_ele = 1
#                    return 1 + 1 = 2
#                                  ↑
#                    small_ele = 2
#                    return 2 + 1 = 3
#
# Final answer = 3

# and for not found case

# [] → return -1
#       ↑
# small_ele = -1 → return -1
#       ↑
# small_ele = -1 → return -1
#
# Final answer = -1