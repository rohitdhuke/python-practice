def find_x(arr,x):
    if len(arr)==0:
        return False
    if arr[0]==x:
        return True
    small_op=find_x(arr[1:],x)
    return small_op


arr=[10,20,30,40]
print(find_x(arr,40))