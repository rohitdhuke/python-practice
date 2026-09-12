def sum_arr(arr):
    if len(arr) == 0:
        return 0

    # Start from index 1 and go until the end
    small_ele = sum_arr(arr[1:])

    # Add current first element to returned sum
    tot_sum = arr[0] + small_ele

    return tot_sum


arr = [22, 58, 14, 36, 8, 5, 144, 55]
print(sum_arr(arr))