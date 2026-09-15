def first_occur(arr,target):
    first=-1
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            first=mid
            high=mid-1
        elif arr[mid]<target:
            low=mid+1

        else:
            high=mid-1

    last=-1
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            last=mid
            low=mid+1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    if first==-1:
        return 0

    return last-first +1



arr = [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
target = 3
print(first_occur(arr, target))


