def is_sorted(arr, si):
    # Stop at the last index because in the previous call
    # arr[si + 1] has already checked this last element.
    if si == len(arr) - 1:
        return True

    if arr[si] > arr[si + 1]:
        return False

    small_ele = is_sorted(arr, si + 1)
    return small_ele


arr = [2, 4, 6, 8, 10]
print(is_sorted(arr, 0))