# arr = [1, 2, 3, 2, 4, 1, 5]
# # for i in range  (len(arr)):
# i=0
# while i<len(arr):
#     j=i+1
#     #for j in range (i+1,len(arr)):
#     while j<len(arr):
#         if arr[i] == arr[j]:
#             arr.pop(j)
#
#         else:
#
#             j=j+1
#     i=i+1
#
# print(arr)

# def removeduplicate(arr):
#     i=0
#     while i<len(arr):
#         j=i+1
#         while j<len(arr):
#             if arr[i]==arr[j]:
#                 arr.pop(j)
#
#             else:
#                 arr.append(arr[i])
#                 j+=1
#         i+=1
#     return arr
# arr = [1, 2, 3, 2, 4, 1, 5]
# removeduplicate(arr)
# print(arr)

#create new list of unique element

# li=[1,2,3,5,1,2,5,46,55,6,2]
# newli=[]
# i=0
# while i<len(li):
#     if li[i] in newli:
#         pass
#     else:
#         newli.append(li[i])
#     i+=1
# print(newli)

# s='programming'
# ns=''
# i=0
# while i<len(s):
#     if s[i] not in ns:
#         ns += s[i]
#
#
#     i+=1
# print(ns)
# # Interview point
#
# If the interviewer says:
#
# "Remove duplicates from a string without creating a new string."
#
# You should mention:
#
# Python strings are immutable, so characters cannot be removed from the original string in place.
# Your task: Find the first non-repeating character.
s = "aabbcddee"
i=0
while i<len(s):
    count=0
    j=0
    while j<len(s):
        if s[i]==s[j]:
            count+=1
        j+=1
    if count ==1:
        print(s[i])
        break
    i+=1








