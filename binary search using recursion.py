def binary_search(arr,target,si,ei):
    if si > ei:
        return -1
    mid= (si+ei)//2
    if target==arr[mid]:
        return mid
    elif target>arr[mid]:
        return binary_search(arr,target,mid + 1,ei)
    else:
        return binary_search (arr,target,si,mid - 1)
arr = [10, 20, 30, 40, 50, 60, 70]
target = 100
print(binary_search(arr,target,0,len(arr)-1))