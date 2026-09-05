# ============================================================
# 1. SPACE-SEPARATED INPUT
# ============================================================

# Example Input:
# Enter number of elements: 4
# Enter 4 numbers separated by space: 10 20 30 40

n = int(input("Enter number of elements: "))

li = [int(x) for x in input(f"Enter {n} numbers separated by space: ").split()]
# input()       -> "10 20 30 40"
# split()       -> ["10", "20", "30", "40"]
# int(x)        -> converts each value to integer
# Final li      -> [10, 20, 30, 40]

print(li)


# ============================================================
# 2. LINE-SEPARATED INPUT
# ============================================================

# Example Input:
# Enter number of elements: 4
# Enter number: 10
# Enter number: 20
# Enter number: 30
# Enter number: 40

n = int(input("Enter number of elements: "))

li = [int(input("Enter number of line separated: ")) for i in range(n)]
# range(n)      -> runs n times
# input()       -> takes one value on each line
# int(input())  -> converts each value to integer
# Final li      -> [10, 20, 30, 40]

print(li)