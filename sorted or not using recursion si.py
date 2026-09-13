def is_sorted(arr, si):
    if si == len(arr) - 1:
        return True

    if arr[si] > arr[si + 1]:
        return False

    return is_sorted(arr, si + 1)
arr=[10,220,30,40]
print(is_sorted(arr,0))