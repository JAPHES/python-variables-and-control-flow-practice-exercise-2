def find_largest_number(numbers):
    largest = numbers[0]  # Start by assuming the first number is the largest
    for num in numbers:    # Loop through each number in the tuple
        if num > largest:  # If the current number is larger than the largest found so far
            largest = num   # Update largest
    return largest

# Example usage
numbers = (10, 20, 30, 40, 50)
largest_number = find_largest_number(numbers)
print(largest_number)  # Output: 50
