arr = [
    [12, 5, 8, 3],
    [7, 15, 4, 9],
    [6, 2, 18, 11],
    [10, 14, 1, 20]
]
row_index = 0
col_index = 0
target = 20
flag=False
for i in range (len(arr)):
    for j in range (len(arr[i])):
        if target == arr[i][j]:
            row_index = i
            col_index = j
            # print(f'target found, row_index = {row_index}, col_index = {col_index}')
            flag = True
            break
    if flag:
        break
if flag:
    print(f'target found, row_index = {row_index}, col_index = {col_index}')
else:
    print("Not Found")


