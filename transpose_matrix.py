arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# j represents the column index
for j in range(len(arr[0])):

    # If column index is even (0, 2, 4...)
    # Move from top to bottom
    if j % 2 == 0:

        # i represents the row index
        # i moves: 0 -> 1 -> 2
        for i in range(len(arr)):
            print(arr[i][j], end=" ")

    # If column index is odd (1, 3, 5...)
    # Move from bottom to top
    else:

        # i moves backwards: 2 -> 1 -> 0
        for i in range(len(arr) - 1, -1, -1):
            print(arr[i][j], end=" ")