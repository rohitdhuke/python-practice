# # ============================================================
# # FIND UNIQUE ELEMENT IN A LIST
# # ============================================================
#
# def findUnique(arr, n):
#
#     # Pick each element one by one
#     for i in range(n):
#
#         j = 0
#
#         # Compare arr[i] with every other element
#         while j < n:
#
#             # Same value found at a different index = duplicate
#             if i != j and arr[i] == arr[j]:
#                 break
#
#             j += 1
#
#         # If j reached n, no duplicate was found
#         if j == n:
#             return arr[i]
#
#     return -1
#
#
# arr = [2, 3, 1, 6, 3, 6, 2]
# n = len(arr)
#
# unique = findUnique(arr, n)
#
# print(unique)       # Output: 1

# ============================================================
# FIND UNIQUE ELEMENT USING COUNT()
# ============================================================

def findUnique(arr, n):

    # Check each element
    for i in range(n):

        # If element occurs only once, it is unique
        if arr.count(arr[i]) == 1:
            return arr[i]

    return -1


arr = [2, 3, 1, 6, 3, 6, 2]
n = len(arr)

unique = findUnique(arr, n)

print(unique)       # Output: 1