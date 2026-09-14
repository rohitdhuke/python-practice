def last_occur(arr, k,si):
    if si==len(arr):
        return -1

    small_ele=last_occur(arr,k,si + 1)

    if small_ele != -1:
        return small_ele

    if arr[si]==k:
        return si
    return -1


arr = [5, 2, 7, 2, 9, 2]
print(last_occur(arr, 2,0))

