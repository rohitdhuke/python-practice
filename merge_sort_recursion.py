# Problem Statement:
# Sort the given array in ascending order using Merge Sort with recursion.

def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Divide array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursive calls
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge sorted halves
    arr3 = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr3.append(right[j])
            j += 1
        else:
            arr3.append(left[i])
            i += 1

    # Add remaining elements
    while i < len(left):
        arr3.append(left[i])
        i += 1

    while j < len(right):
        arr3.append(right[j])
        j += 1

    return arr3


arr = [9, 3, 7, 5, 2]
print(merge_sort(arr))


# Merge Sort using Recursion:
# DIVIDE → RECURSIVE CALLS → MERGE → RETURN SORTED ARRAY