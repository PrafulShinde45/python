def binary_search(arr, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Input from user
n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
x = int(input("Enter the element to search for: "))

# Perform binary search
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")
