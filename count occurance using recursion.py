#using SI
from idlelib.debugger_r import debugging


# def find_x(arr,x,si,count):
#     if si==len(arr):
#         return count
#     if arr[si]==x:
#         count+=1
#
#     small_ele=find_x(arr,x,si+1,count)
#     return small_ele
#
# arr = [5, 2, 7, 2, 9, 2]
# print(find_x(arr,2,0,0))

# arr always stays: [5, 2, 7, 2, 9, 2]
#
# si    arr[si]    si==len(arr)    match?      count
# ────────────────────────────────────────────────────
# 0       5          0==6 False     5==2 ❌       0
# 1       2          1==6 False     2==2 ✅       1
# 2       7          2==6 False     7==2 ❌       1
# 3       2          3==6 False     2==2 ✅       2
# 4       9          4==6 False     9==2 ❌       2
# 5       2          5==6 False     2==2 ✅       3
# 6       -          6==6 True ✅                3
#                                                 ↓
#                                              return 3

#                     BASE
#                      3
#                      ↑
# si=5 → small_ele = 3 → return 3
#                      ↑
# si=4 → small_ele = 3 → return 3
#                      ↑
# si=3 → small_ele = 3 → return 3
#                      ↑
# si=2 → small_ele = 3 → return 3
#                      ↑
# si=1 → small_ele = 3 → return 3
#                      ↑
# si=0 → small_ele = 3 → return 3
#
# Final = 3




#with slicing
# def find_x(arr,x,count):
#     if len(arr)==0:
#         return count
#     if arr[0]==x:
#         count+=1
#     small_elem=find_x(arr[1:],x,count)
#     return small_elem
# arr = [5, 2, 7, 2, 9, 2]
# print(find_x(arr,2,0))

# debugging line by line

# arr                      len(arr)    len(arr)==0    count
# ──────────────────────────────────────────────────────────
# [5,2,7,2,9,2]               6          False         0
# [2,7,2,9,2]                 5          False         1
# [7,2,9,2]                   4          False         1
# [2,9,2]                     3          False         2
# [9,2]                       2          False         2
# [2]                         1          False         3
# []                          0          True  ✅       3
#                                                    ↓
#                                                 return 3



# SLICING VERSION              si VERSION
#
# arr gets smaller             arr stays SAME
#       ↓                            ↓
# [5,2,7,2,9,2]               si = 0
# [2,7,2,9,2]                 si = 1
# [7,2,9,2]                   si = 2
# [2,9,2]                     si = 3
# [9,2]                       si = 4
# [2]                         si = 5
# []                          si = 6
#  ↓                            ↓
# len(arr)==0                 si==len(arr)