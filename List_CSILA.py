original = input("Original list:")
new_index = int(input("Input Index to Update: "))
index_val = input("Input New Value: ")
slice_range1 = int(input("Enter Slice Range 1: "))
slice_range2 = int(input("Enter Slice Range 2: "))
search = input("Input Search Item: ")

print(f"Updated index {new_index}")
print(f"Replacement value: {index_val}")

original = original.split()
print(original)

original[new_index] = index_val
new_list = original[slice_range1:slice_range2]

print(f"Sliced List {slice_range1}:{slice_range2} = {new_list}")

if search in new_list:
    print(f"Search result (from sliced array): {search} is present in the sliced list.")
else:
    print(f"Search result (from sliced array): {search} is not present in the sliced list.")

print(f"New List: {original}")
