def last_occur(arr, k):

    # Base case: array is empty, so k was not found
    if len(arr) == 0:
        return -1

    # Go to the end first; checking happens during unwinding
    small_ele = last_occur(arr[1:], k)

    # small_ele stays -1 until a match is found.
    # Once a match returns 0, each previous recursive call adds 1
    # during unwinding to rebuild/maintain the original index.
    if small_ele != -1:
        return small_ele + 1

    # If the smaller array did not find k,
    # check the current first element.
    if arr[0] == k:
        return 0

    # k was not found
    return -1


arr = [5, 2, 7, 2, 9, 2]
print(last_occur(arr, 2))