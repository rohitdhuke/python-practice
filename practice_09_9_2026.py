# Que 01: How many even numbers are there?
# arr = [4, 7, 2, 9, 6, 3, 8]
# count_even=0
# for i in range (len(arr)):
#     if arr[i] % 2 == 0:
#         count_even += 1
# print(count_even)
#         # print(arr[i],': even')
#     # else:
#     #     print(arr[i],': odd')


# Que 02: Find the sum of only the even numbers.
# arr = [12, 5, 8, 21, 14, 7, 10]
# cal_even=0
# cal_odd=0
# for i in range (len(arr)):
#     if arr[i] % 2 == 0:
#         cal_even += arr[i]
#     else:
#         cal_odd += arr[i]
# print(cal_even)
# print(cal_odd)

# Question 3 — Count Numbers Greater Than a Given Value
# arr = [15, 7, 22, 10, 35, 8, 19]
# x = 10
# count=0
# for i in range (len(arr)):
#     if arr[i] > x:
#         count += 1
# print(count)

# Question 4 — Find the Largest Number Without max()
# arr = [18, 42, 7, 31, 56, 23]
# max_ele=arr[0]
# for i in range (len(arr)):
# # for i in range(1,len(arr)): #we already stored arr[0] in max_ele
#     if arr[i] > max_ele:
#         max_ele = arr[i]
# print(max_ele)

# Que 05: Find the smallest element without using min() or sorting.
# arr = [34, 12, 67, 5, 29, 18]
# min_ele=arr[0]
# for i in range(1,len(arr)):
#     if arr[i]<min_ele:
#         min_ele=arr[i]
# print(min_ele)

# Question 6 — Find the Second Largest Element
# arr = [12, 35, 1, 10, 34, 2]
# large_ele=arr[0]
# second_large_ele=arr[1]
# if arr[0] > arr[1]:
#     large_ele=arr[0]
#     second_large_ele=arr[1]
# else:
#     large_ele=arr[1]
#     second_large_ele=arr[0]
# for i in range(2,len(arr)):
#     if arr[i]>large_ele:
#         second_large_ele = large_ele
#         large_ele=arr[i]
#     elif arr[i] > second_large_ele:
#          second_large_ele=arr[i]
# print(second_large_ele)

# Question 7 — Count Positive, Negative, and Zero
#
# Problem Statement:
# Given a list of integers, write a Python program to count how many numbers are positive, negative, and zero.

# arr = [10, -5, 0, 7, -3, 0, -8, 12]
# pos_cnt = 0
# neg_cnt = 0
# zero_cnt = 0
# for i in range(len(arr)):
#     if arr[i] > 0:
#         pos_cnt += 1
#     elif arr[i] < 0:
#         neg_cnt += 1
#     else:
#         zero_cnt += 1
# print('positive cnt:', pos_cnt)
# print('negative cnt:', neg_cnt)
# print('zero cnt:', zero_cnt)

# Question 8 — Find the Sum of Elements at Even Indexes
#
# Problem Statement:
# Given a list of integers, write a Python program to calculate the sum of elements present at even indexes
# arr = [10, 20, 30, 40, 50, 60, 70]
# tot_even = 0
# for i in range (len(arr)):
#     if i % 2 == 0:
#         tot_even += arr[i]
# print(tot_even)
#
# Question 9 — Count Occurrences of a Number
#
# Problem Statement:
# Given a list and a target number, write a Python program to find how many times the target appears in the list.

# arr = [4, 2, 7, 4, 9, 4, 2, 4]
# target = 4
# cnt_tgt=0
# for i in range(len(arr)):
#     if arr[i] == target:
#         cnt_tgt += 1
# print(cnt_tgt)

# Find the First Occurrence of a Target
#
# Problem Statement:
# Given a list and a target value, write a Python program to find the index of the first occurrence of that target.
#
# arr = [10, 25, 7, 25, 40, 25]
# target = 25
# for i in range (len(arr)):
#     if arr[i] == target:
#         print('index of', target ,'is: ',i)
#         break

# Question 11 — Find Whether an Element Exists
#
# Problem Statement:
# Given a list and a target value, write a Python program to check whether the target exists in the list.

# arr = [11, 4, 18, 7, 25, 9]
# target = 18
# for i in range (len(arr)):
#     if arr[i] == target:
#         print('found')
#         break
# else:
#     print('not found')

# Question 12 — Reverse a List Without reverse()
#
# Problem Statement:
# Given a list of integers, write a Python program to print the elements in reverse order without using reverse() or slicing [::-1].
#
# arr = [10, 20, 30, 40, 50]
# print(len(arr))
# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i], end=" ")
# arr = [10, 20, 30, 40, 50]
# for i in range (len(arr)):
#     print(arr[i])
# len(arr) = how many elements.
# len(arr) - 1 = index of the last element.

# Question 13 — Store the Reversed List
#
# Problem Statement:
# Given:

# arr = [5, 10, 15, 20, 25]
# rev_lst=[]
# for i in range(len(arr)-1, -1, -1):
#     rev_lst.append(arr[i])
# print(rev_lst)

# Question 14 — Find Sum of First and Last Element
#
# Problem Statement:
# Given a list of integers, write a Python program to calculate the sum of the first and last elements.

# arr = [15, 20, 35, 40, 55]
# a=arr[0]
# b=arr[len(arr)-1]
# print(a+b)


# a=arr[0]
# b=arr[-1]
# c=a+b
# print(c)


# fst_ele=arr[0]
# for i in range(len(arr)-1,-1,-1):
#     lst_ele=arr[i]
#     break
# tot=fst_ele + lst_ele
# print(tot)

# Question 15 — Count Elements Between Two Values
#
# Problem Statement:
# Given a list of integers, count how many elements are greater than 10 and less than 30.

# arr = [5, 12, 25, 30, 18, 7, 40, 22]
# cnt=0
# for i in range(len(arr)):
#     if arr[i] > 10 and arr[i] < 30:
#         cnt+=1
# print(cnt)


# Question 16 — Find the Difference Between Maximum and Minimum
#
# Problem Statement:
# Given a list of integers, find the difference between the largest and smallest elements without using max(), min(), or sorting.

# arr = [23, 5, 17, 42, 9, 30]
# min=arr [0]
# max=arr [1]
# diff=0
# if min>max:
#     max,min=min,max
# for i in range(2,len(arr)):
#     if arr[i]>max:
#         max=arr[i]
#     elif arr[i]<min:
#         min=arr[i]
# diff=max-min
# print(diff)


# Question 17 — Find Duplicate Elements:

# arr = [4, 7, 2, 4, 8, 7, 1]
# for i in range (len(arr)):
#     for j in range (i+1,len(arr)):
#         if arr[i]==arr[j]:
#             print('duplicate found')
#             break
#

# Question 18 — Find Unique Elements
#
# Problem Statement:
# Given a list of integers, print all elements that occur only once in the list.
#
# arr = [4, 7, 2, 4, 8, 7, 1]
# for i in range (len(arr)):
#
#     for j in range (len(arr)):
#         # Check if the same value exists at another index (duplicate found)
#         if i != j and arr[i]==arr[j]:
#            break
#     else:
#         print(arr[i], end=" ")

# Question 19 — Find Common Elements Between Two Lists
#
# Problem Statement:
# Given two lists, write a Python program to print the elements that are present in both lists.

# arr1 = [4, 7, 2, 9, 5]
# arr2 = [8, 2, 4, 10, 7]
#
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if arr1[i] == arr2[j]:
#             print(arr1[i])
#             break

# Question 20 — Find Elements Present in First List but Not Second
#
# Problem Statement:
# Given two lists, print the elements from arr1 that are not present in arr2.

# arr1 = [4, 7, 2, 9, 5]
# arr2 = [8, 2, 4, 10, 7]
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if arr1[i] == arr2[j]:
#             break
#     else:
#         print(arr1[i])

# Question 21 — Remove Duplicates Without set()
#
# Problem Statement:
# Given a list containing duplicate values, create a new list containing each element only once, while maintaining the original order.
# arr = [4, 7, 2, 4, 8, 7, 2, 1]
# unq_arr=[]
#
# for i in range(len(arr)):
#
#     for j in range(len(unq_arr)):
#         if arr[i] == unq_arr[j]:
#             # already exists
#             break
#
#     else:
#         # if loop didn't break → value wasn't found
#         # what should you do here?
#         unq_arr.append(arr[i])
# print(unq_arr)

# Count Duplicate Pairs
#
# Problem Statement:
# Given a list of integers, write a Python program to count how many duplicate pairs are present.

arr = [4, 7, 2, 4, 8, 7, 1]
cnt=0
for i in range (len(arr)):

    for j in range (i+1,len(arr)):
        if arr[i]==arr[j]:
            cnt+=1
print(cnt)

