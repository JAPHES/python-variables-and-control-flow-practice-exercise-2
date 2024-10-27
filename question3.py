def sum_of_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 9, 28, 8, 18, 19,]
result = sum_of_numbers(nums)
print(f"The sum of the numbers is: {result}")
