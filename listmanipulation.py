def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(original_list)
print("Original List:", original_list)
print("List with Duplicates Removed:", result_list)
