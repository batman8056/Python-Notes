# If we don't know what number in the list
# the loop taken n-number of item in the list to find out linerar o(n) (time and space equal)

def check_number(numbers):
    for num in numbers:
        if num == 2:
            return True
        else:
            continue
    return f"number {2} is not present"  # Return False if 2 is not found

# Example usage
number = [1, 3, 4, 2, 5]
print(check_number(number))  # Output: True
