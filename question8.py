def keys_with_value_greater_than(input_dict, n):
    keys_list = []  # Initialize an empty list to store the keys
    for key, value in input_dict.items():  # Iterate over key-value pairs in the dictionary
        if value > n:  # Check if the value is greater than n
            keys_list.append(key)  # If so, add the key to the list
    return keys_list

# Example usage
my_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
result = keys_with_value_greater_than(my_dict, n)
print(result)  # Output: ['a', 'b']
