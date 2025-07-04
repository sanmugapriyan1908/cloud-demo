# Create simple lists (as arrays)
array1 = [1, 2, 3]
array2 = [4, 5, 6]
array3 = [7, 8, 9]

# Add lists to a set (must convert to tuples because lists are unhashable)
array_set = set()
array_set.add(tuple(array1))
array_set.add(tuple(array2))
array_set.add(tuple(array3))

# Display the set of arrays
print("Set of arrays:")
for arr in array_set:
    print(list(arr))
