# O(N) -linear
def check_number_twice(numbers):
        if len(set(numbers)) == len(numbers):
            return False
        else:
            return True

# Example number of list
number = [1, 3, 1, 2, 5]
print(check_number_twice(number)) 