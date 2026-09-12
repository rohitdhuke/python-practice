def is_sorted(arr):

    # Base case:
    # If only one element is left, it is always sorted
    if len(arr) == 1:
        return True

    # Recursive call:
    # Check whether the remaining array from index 1 is sorted
    small_ele = is_sorted(arr[1:])

    # Compare the current first element with the next element
    # If they are in ascending order, return the result
    # received from the recursive call
    if arr[0] <= arr[1]:
        return small_ele

    # If current element is greater than the next element,
    # the array is not sorted
    else:
        return False


arr = [2, 99,4, 6, 8, 10]

# Call the function and print True if sorted, otherwise False
print(is_sorted(arr))

