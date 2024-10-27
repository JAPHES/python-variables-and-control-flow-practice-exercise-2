def remove_duplicates(input_list):
    output_list = []  # Initialize an empty list to store unique elements
    for item in input_list:  # Loop through each item in the input list
        if item not in output_list:  # Check if the item is not already in the output list
            output_list.append(item)  # Add it to the output list if it's unique
    return output_list

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(unique_list)  # Output: [1, 2, 3, 4, 5]
