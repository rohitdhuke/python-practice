arr = [
    [4, 8, 3, 2],
    [7, 6, 5, 1],
    [9, 2, 10, 4],
    [3, 5, 7, 12]
]
secondary_diagonal_sum = 0
for row in range (len(arr)):
    for col in range(len(arr[row])):
        if row + col == len(arr) - 1:
            secondary_diagonal_sum += arr[row][col]
print(f"Sum of secondary_diagonals: {secondary_diagonal_sum}")

