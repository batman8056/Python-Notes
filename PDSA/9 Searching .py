# Binary Search O(log n)

# def binary_search(arr, target, left, right):
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search(arr, target, mid + 1, right)
#     else:
#         return binary_search(arr, target, left, mid - 1)

# arr = [1, 2, 3, 4, 5, 6, 7]
# print(binary_search(arr, 5, 0, len(arr) - 1))  # Output: 4

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid +1, right)
    else:
        return binary_search(arr, target, mid -1, left)



arr = [1, 2, 3, 4, 5, 6, 7]
# print(len(arr))
print(binary_search(arr, 5, 0, len(arr) - 1))  # Output: 4