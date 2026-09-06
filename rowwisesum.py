def rowwisesum(mat):
    # len(mat) gives the number of rows
    for i in range(len(mat)):
        sum = 0
        # len(mat[i]) gives number of columns in current row
        for j in range(len(mat[i])):
            # Add current element
            sum += mat[i][j]
        print(sum,end=' ')

mat=[
    [1,2],
    [3,4],
    [5,6],
    [7,8],
]
rowwisesum(mat)
