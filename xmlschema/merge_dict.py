def merge_dicts(original_dict, new_dict):
    merged_dict = original_dict.copy()  # Make a copy of the original dictionary
    merged_dict.update(new_dict)  # Update the copy with the content of the new dictionary
    return merged_dict

# Example dictionaries
original_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {'b': 20, 'd': 40}

# Merge original_dict with new_dict
merged_dict = merge_dicts(original_dict, new_dict)

print(merged_dict)  # Output: {'a': 1, 'b': 20, 'c': 3, 'd': 40}
