# Input matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix
matrix = []
print("Enter matrix row by row:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# 🔹 Row Sum
print("\nRow Sums:")
for i in range(rows):
    row_sum = 0
    for j in range(cols):
        row_sum += matrix[i][j]
    print(f"Row {i} sum =", row_sum)

# 🔹 Column Sum
print("\nColumn Sums:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Column {j} sum =", col_sum)

# 🔹 Search for a value
key = int(input("\nEnter value to search: "))
found = False
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            print(f"Value found at position ({i}, {j})")
            found = True

if not found:
    print("Value not found")

# 🔹 Transpose (Conceptual Output)
print("\nTranspose of Matrix:")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()   