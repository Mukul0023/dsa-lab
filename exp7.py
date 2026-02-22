def insert_element(arr, pos, value):
    shifts = 0
    n = len(arr)

    if pos < 0 or pos > n:
        print("Invalid position")
        return arr, 0

    arr.append(None)  # increase size

    # Shift elements right
    for i in range(n, pos, -1):
        arr[i] = arr[i-1]
        shifts += 1

    arr[pos] = value
    return arr, shifts 


def delete_element(arr, pos): 
    shifts = 0
    n = len(arr)

    if pos < 0 or pos >= n:
        print("Invalid position")
        return arr, 0

    # Shift elements left
    for i in range(pos, n-1):
        arr[i] = arr[i+1]
        shifts += 1

    arr.pop()
    return arr, shifts


# 🔹 Input
arr = list(map(int, input("Enter elements: ").split()))
choice = input("Type insert/delete: ").lower()

if choice == "insert":
    pos = int(input("Enter position: "))
    value = int(input("Enter value: "))
    arr, shifts = insert_element(arr, pos, value)
    print("Updated List:", arr)
    print("Shift Count:", shifts)

elif choice == "delete":
    pos = int(input("Enter position: "))
    arr, shifts = delete_element(arr, pos)
    print("Updated List:", arr)
    print("Shift Count:", shifts) 