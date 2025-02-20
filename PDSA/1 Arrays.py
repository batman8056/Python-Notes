# Find the Missing Number O(n)

# def find_missing(arr, n):
#     total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
#     print(total_sum)
#     return total_sum - sum(arr)

# arr = [1, 2, 4, 5, 6]
# n = 6
# print(find_missing(arr, n))  # Output: 3

def find_missing(arr , n):
    total_sum = n * (n+1) // 2
    return total_sum - sum(arr)
arr = [1, 2, 4, 5, 6]
n = 6
print(find_missing(arr, n))