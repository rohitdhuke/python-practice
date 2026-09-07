# # Problem: Column-Wise Sum of a 2D Array
# #
# # Given a 2D integer array arr of size N × M, calculate and print the sum of the elements in each column.
# #
# # Print all column sums on a single line, separated by a space.
#
# # 2D list (matrix)
# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # Outer loop traverses each column
# # len(arr[0]) gives the number of columns
# for j in range(len(arr[0])):
#
#     # Reset column_sum to 0 for every new column
#     column_sum = 0
#
#     # Inner loop traverses each row
#     # len(arr) gives the number of rows
#     for i in range(len(arr)):
#
#         # Add the current element to the column sum
#         # i = row index, j = column index
#         column_sum += arr[i][j]
#
#     # Print the sum of each column on the same line
#     print(column_sum, end=" ")
#
# Given a two-dimensional integer array arr, calculate and print the sum of the elements in each row.
#
# Print all row sums on a single line, separated by a space.
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Outer loop traverses each row
# for row in range(len(arr)):
#
#     # Reset sum for every new row
#     row_sum = 0
#
#     # Inner loop traverses each element/column of current row
#     for elem in range(len(arr[row])):
#
#         # Add current element to row sum
#         row_sum += arr[row][elem]
#
#     # Print each row sum on the same line
#     print(row_sum, end=' ')
