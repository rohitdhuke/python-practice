# ============================================================
# 1. NEW LIST IS NOT STORED
# ============================================================

def change(li):
    li[1] = li[1] + 2
    li = [3, 3, 3, 4, 5]
    return li

li = [1, 2, 3, 4, 5]

change(li)                 # Returned list is NOT stored

print(li)                  # Output: [1, 4, 3, 4, 5]


# ============================================================
# 2. NEW LIST IS STORED
# ============================================================

def change(li):
    li[1] = li[1] + 2
    li = [3, 3, 3, 4, 5]
    return li

li = [1, 2, 3, 4, 5]

li = change(li)            # Returned list IS stored in global li

print(li)                  # Output: [3, 3, 3, 4, 5]