# Problem Statement:
# Sort the given array in ascending order using Insertion Sort.
arr = [9, 3, 7, 5, 2]

for i in range(1, len(arr)):
    temp = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > temp:
        # Shift bigger element one position to the right
        arr[j + 1] = arr[j]

        # Move left to find the correct position
        j = j - 1

    # Insert temp at its correct position
    arr[j + 1] = temp

print(arr)

# arr[j+1] = arr[j] → Shift bigger value right (temporary duplicate)
# j -= 1            → Move backward to check previous element
# arr[j+1] = temp    → Insert temp at its correct position

# Insertion Sort → SAVE temp → CHECK backward → SHIFT bigger values right → INSERT temp.
