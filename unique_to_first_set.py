# # Given two lists of integers, find the elements that are
# # present in the first list but NOT present in the second list.
# #
# # Input:
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 60, 70]
# #
# # Expected Output:
# # {10, 20, 50}
# #
# # Requirements:
# # 1. Convert both lists into sets.
# # 2. Use a set operation.
# # 3. Do not use loops.
# # 4. Print the result.
# set1=set(list1)
# set2=set(list2)
# unique_set = set1.difference(set2)
# print(unique_set)
#
#
s = set()
s.add(4)
s.add(4)
print(len(s))