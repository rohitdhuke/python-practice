# ============================================================
# SWAP ALTERNATE ELEMENTS IN A LIST
# ============================================================

def swapAlternate(arr, n):

    # Start from index 0, move by 2
    for i in range(0, n - 1, 2):

        # Swap current element with next element
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr = [1, 2, 3, 4, 5, 6]    # Original list
n = len(arr)                  # Number of elements = 6

swapAlternate(arr, n)         # Function modifies the original list

print(arr)                    # Output: [2, 1, 4, 3, 6, 5]