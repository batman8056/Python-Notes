# QuickSort

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2] #arr[3]
#     print(pivot) # 10
#     left = [x for x in arr if x < pivot]
#     print(f"the left value {left}")
#     middle = [x for x in arr if x == pivot]
#     print(f"middle of the value {middle}")
#     right = [x for x in arr if x > pivot]
#     print(f"the right side of the value {right}")
#     return quicksort(left) + middle + quicksort(right)

# arr = [3, 6, 8, 10, 1, 2, 12]
# print(quicksort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))  # Output: [1, 1, 2, 3, 6, 8, 10]

