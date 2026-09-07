arr = [
    [4, 8, 3, 2],
    [7, 6, 5, 1],
    [9, 2, 10, 4],
    [3, 5, 7, 12]
]
diagonal_sum = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i==j:
            diagonal_sum += arr[i][j]
print(f"Main diagonal sum: {diagonal_sum}")
