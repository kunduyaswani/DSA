# Array Operations in Python

arr = [10, 20, 30, 40, 50]

# Display
print("Original Array:", arr)

# Traverse
print("Traversing Array:")
for i in arr:
    print(i, end=" ")
print()

# Insertion
arr.insert(2, 25)
print("After Insertion:", arr)

# Deletion
arr.pop(3)
print("After Deletion:", arr)

# Linear Search
key = 40
if key in arr:
    print(key, "is found at index", arr.index(key))
else:
    print(key, "is not found")

# Update
arr[1] = 100
print("After Update:", arr)

# Maximum Element
print("Maximum Element:", max(arr))

# Minimum Element
print("Minimum Element:", min(arr))

# Sum of Elements
print("Sum of Elements:", sum(arr))

# Reverse Array
arr.reverse()
print("Reversed Array:", arr)

# Sort Array
arr.sort()
print("Sorted Array:", arr)

# Length of Array
print("Length of Array:", len(arr))