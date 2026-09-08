# Given a list of integers, remove all duplicate elements using a set.
#
# Input:
li = [10, 20, 30, 20, 40, 10, 50, 30]
#
# Expected Output:
# {10, 20, 30, 40, 50}
#
# Requirements:
# 1. Create the given list.
# 2. Use a set to remove duplicate elements.
# 3. Print the resulting set.
s=set()
print(type(s))
for number in li:
    s.add(number)
print(s)
