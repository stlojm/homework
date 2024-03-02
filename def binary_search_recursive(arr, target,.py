def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14
print(binary_search_recursive(arr, target, 0, len(arr) - 1))  # Output will be 6 (index of 14 in the array)
