def binary_search(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high = mid-1
        else:
            low = mid+1
    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
x = 23
print(binary_search(arr, x))
