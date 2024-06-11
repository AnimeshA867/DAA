import time

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Input values
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# Measure the time taken to execute the Binary Search function
start_time = time.time()
result = binary_search(arr, target)
end_time = time.time()

# Output the result and time taken
if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the list")
print(f"Time taken to perform binary search: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
