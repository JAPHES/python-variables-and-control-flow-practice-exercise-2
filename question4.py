
def reverse_strings(string_list):
    return [s[::-1] for s in string_list]

# Example usage
input_list = ["apple", "banana", "cherry"]
reversed_list = reverse_strings(input_list)
print(reversed_list)  # Output: ['elppa', 'ananab', 'yrrehc']
