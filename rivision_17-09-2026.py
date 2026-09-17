# Bubble Sort
# Problem: Sort the array in ascending order

arr = [64, 34, 25, 12, 22, 11, 90]

# Outer loop controls the number of passes
for i in range(len(arr) - 1):

    # After every pass, the largest remaining element
    # reaches the end, so we reduce the checking range by i
    for j in range(len(arr) - i - 1):

        # Compare two neighboring elements
        if arr[j] > arr[j + 1]:

            # Swap if the left element is greater than the right element
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Print the sorted array
print(arr)


# Bubble Sort = compare neighbors → swap → largest moves to the right.



# Selection Sort
# Problem: Sort the array in ascending order

arr = [64, 25, 12, 22, 11]

# Outer loop selects the position where
# the smallest element should be placed
for i in range(len(arr)):

    # Assume the current element is the smallest
    # min stores the INDEX of the smallest element
    min = i

    # Search for a smaller element in the remaining array
    for j in range(i + 1, len(arr)):

        # If a smaller element is found
        if arr[min] > arr[j]:

            # Store its index as the new minimum
            min = j

    # Swap the smallest element with the current position
    # This happens only after checking the remaining array
    arr[i], arr[min] = arr[min], arr[i]

# Print the sorted array
print(arr)


# Selection Sort
#
# i → current position
# min → index of smallest element
# j → searches remaining elements
#
# Find smallest
#      ↓
# remember its index
#      ↓
# finish inner loop
#      ↓
# swap with arr[i]


# Insertion Sort
# Problem: Sort the array in ascending order

arr = [5, 3, 8, 2]

# Start from index 1 because the first element
# is considered already sorted
for i in range(1, len(arr)):

    # Store the current value that we want to insert
    # into the correct position
    key = arr[i]

    # Start checking from one position left of i
    j = i - 1

    # Shift all elements greater than key
    # one position to the right
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]

        # Move j toward the left
        j -= 1

    # Insert key into its correct position
    # j has moved one position too far left,
    # so the correct position is j + 1
    arr[j + 1] = key

# Print the sorted array
print(arr)



# Insertion Sort
#
# key = current VALUE
#         ↓
# j = one position LEFT
#         ↓
# Is arr[j] > key?
#         ↓ yes
# shift arr[j] RIGHT
#         ↓
# move j LEFT
#         ↓
# repeat
#         ↓
# put key at j + 1


# Push all zeros to the end of the array
# Keep all non-zero elements in the same order

arr = [5, 0, 7, 0, 0, 3, 9, 0, 2]

# 'zero' stores the position where
# the next non-zero element should be placed
zero = 0

# 'non_zero' scans every element in the array
for non_zero in range(len(arr)):

    # If the current element is non-zero
    if arr[non_zero] != 0:

        # Swap the non-zero element with the position
        # where the next non-zero should be placed
        arr[zero], arr[non_zero] = arr[non_zero], arr[zero]

        # Move to the next available position
        zero += 1

# Print the final array
print(arr)


# non_zero = searches → zero = waits → non-zero found = swap → zero moves forward.




# Push all 5s to the end of the array

arr = [5, 8, 2, 5, 7, 5, 3, 9, 5, 1]

# Keeps track of where the next non-5 element should be placed
insert_pos = 0

# Scan every element in the array
for current in range(len(arr)):

    # If the current element is not 5
    if arr[current] != 5:

        # Move the non-5 element to the front
        # and move 5 towards the end
        arr[insert_pos], arr[current] = arr[current], arr[insert_pos]

        # Next non-5 should be placed at the next position
        insert_pos += 1

print(arr)


# Push 0s:
# current != 0 → bring non-zero forward
#
# Push 5s:
# current != 5 → bring non-5 forward
#
#
# current     → scans every element
# insert_pos  → waits at the position
#               where the next non-5 should go