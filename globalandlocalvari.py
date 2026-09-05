# ============================================================
# PASSING IMMUTABLE VARIABLE THROUGH FUNCTION
# ============================================================

# 1. RETURN VALUE IS STORED

def increment(a):          # Local a receives value 2
    a = a + 2              # Local a becomes 4
    return a               # Returns 4

a = 2                      # Global a = 2
a = increment(a)           # Returned 4 is stored in global a
print(a)                   # Output: 4


# 2. RETURN VALUE IS NOT STORED

def increment(a):          # Local a receives value 2
    a = a + 2              # Local a becomes 4
    return a               # Returns 4

a = 2                      # Global a = 2
increment(a)               # Returned 4 is not stored
print(a)                   # Global a is still 2 → Output: 2