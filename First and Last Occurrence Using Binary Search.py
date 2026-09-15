def first_occur(arr,target):
    ans=-1
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            ans=mid
            high=mid-1
        elif arr[mid]<target:
            low=mid+1

        else:
            high=mid-1


    return ans
def last_occur(arr,target):
    ans=-1
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            ans=mid
            low=mid+1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return ans



arr = [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
target = 3
print(last_occur(arr, target),first_occur(arr, target))


