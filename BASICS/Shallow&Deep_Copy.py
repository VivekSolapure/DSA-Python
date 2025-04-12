import copy

# Original list with a nested list
original_list = [1, 2, [3, 4]]

# Shallow copy
shallow_copied_list = copy.copy(original_list)

# Deep copy
deep_copied_list = copy.deepcopy(original_list)

print("Original list:", original_list)

# Modifying the nested list in the shallow copy
shallow_copied_list[2][0] = 99

# Modifying the nested list in the deep copy
deep_copied_list[2][1] = 88

print("Shallow copied list:", shallow_copied_list)
print("Original list:", original_list)
print("Deep copied list:", deep_copied_list)
print("Original list:", original_list)

