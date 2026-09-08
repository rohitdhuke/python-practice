# Given two lists of integers, find the common elements
# between them using sets.
#
# Input:
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

# Expected Output:
# {30, 40, 50}
#
# Requirements:
# 1. Create both lists.
# 2. Convert them into sets.
# 3. Find the common elements.
# 4. Print the result.
#
# Do not use nested loops.
set1=set(list1)
set2=set(list2)
common=set(list1) & set(list2)
print(common)