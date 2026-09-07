# Practice 3 — Largest Element in a 2D Array
#
# Given a 2D integer array arr, find the largest element in the entire array and print:
#
# The largest value
# Its row index
# Its column index
#
# If the largest value occurs more than once, choose the first occurrence.

arr = [
    [3, 8, 2, 5],
    [7, 1, 9, 4],
    [6, 9, 3, 2]
]

# main code begin here
row_index = 0
col_index = 0
large_ele=arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr[i])):

        if large_ele < arr[i][j]:
            large_ele = arr[i][j]
            col_index = j
            row_index = i

print(f'largest ele {large_ele},row index {[row_index]},column index{[col_index]}')


# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end=' ')

