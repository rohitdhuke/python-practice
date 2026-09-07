arr = [
    [4, 7, 2, 9],
    [6, 3, 8, 5],
    [1, 10, 12, 11]
]
even_count=0
odd_count=0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]%2==0:
            even_count+=1
        else:
            odd_count+=1
print(f'Even elements:, {even_count} Odd elements: {odd_count}')

# i              → row index
# j              → column index
# arr[i]         → current row
# arr[i][j]      → current element
# % 2 == 0       → even