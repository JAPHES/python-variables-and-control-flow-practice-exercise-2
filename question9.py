def has_pair_with_sum(nums, target_sum):
    seen_numbers = set()  # Create an empty set to store seen numbers
    for num in nums:      # Iterate through each number in the list
        complement = target_sum - num  # Calculate the complement needed to reach the target sum
        if complement in seen_numbers:  # Check if the complement has already been seen
            return True  # If yes, return True
        seen_numbers.add(num)  # Add the current number to the set
    return False  # If no pair is found, return False

# Example usage
numbers = [1, 2, 3, 4, 5]
target = 9
result = has_pair_with_sum(numbers, target)
print(result)  # Output: False
