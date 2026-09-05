row = int(input())
col = int(input())
inputL = list(str(input("Enter values")))
    #.split()
print(type(inputL))
    # .split()

fnlList = []
for i in range(row):
    row_list = []
    # print(row_list)
    print(f"outer loop i row val {i}")
    for j in range(col):
        print(f"inner loop j col val {j }")
        # Flattened index math: row_index * total_columns + column_index
        element = int(inputL[i * col + j])
        print(inputL[i * col + j])
        print(f"element val {element}")
        row_list.append(element)
    fnlList.append(row_list)
print(fnlList)