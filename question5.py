def print_even_keys(input_dict):
    for key, value in input_dict.items():
        if value % 2 == 0:  # Check if the value is even
            print(key)

# Example usage
example_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_keys(example_dict)  # Output: 'a' and 'c'
