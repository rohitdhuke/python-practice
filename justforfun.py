# total=0
# for i in range(len(li)):
#     total=sum(li)
# print(total)

# li=[1,2,3,4,5,6,7,8,9,10]
# target=55
# for i in range(len(li)):
#     if target == li[i]:
#         print (i)
#         break
# else:
#     print(-1)

# li=[1,2,3,4]
# li=[3,3,4]
# li[2]=99
# print(li)
#
# a=347
# x=347
# print(id(a))
# print(id(x))
#
# li=[1,2,3]
# li=[1,2,3]
# print(id(li))
# print(id(li))

# def increament(a):
#     a=a+2
#     print('id of a inside the function: ',id(a),a)
#     return a
#
# a=100
# print('id of a before calling the function: ',id(a))
# x=increament(a)
# print(f'after calling the function: id of a {id(a)}  id of x: {id(x)},value of x: {x}')
#
# def increament(li):
#     li.extend([5,6,7])
#     print('li inside function: ',id(li))
#     # return li
#
# li=[1,2,3,4]
# print('li before calling function: ',id(li))
# increament(li)
# print('li after calling the funcation: ',id(li),li)

# li=[1,2,3,4,5,6]
# # print(li[::-1])
# print(len(li)-1)
#
# for i in range(len(li)-1,-1,-1):
#     print(li[i])


# li=[1,2,3,4,5,6,7,8,9,10]
# for i in range (0,len(li)-1,2):
#     li[i],li[i+1]=li[i+1],li[i]
# print(li)

# find duplicate
# arr = [0, 7, 2, 5, 4, 7, 1, 3, 6]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if i != j and arr[i] == arr[j]:
#             print(arr[i])
#             break

