def is_sorted(arr):
    if len(arr)<=1:
        return True
    if arr[0]>arr[1]:
        return False
    small_ele=is_sorted(arr[1:])
    return small_ele

arr = [2, 4, 6, 8, 10]
print(is_sorted(arr))