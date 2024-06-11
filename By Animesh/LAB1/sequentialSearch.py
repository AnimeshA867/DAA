import time

def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Input values
arr = [1, 2, 3, 4, 5]
target = 3

# Measure the time taken to execute the Sequential Search function
start_time = time.time()
result = sequential_search(arr, target)
end_time = time.time()

# Output the result and time taken
if result != -1:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in the list")
print(f"Time taken to perform sequential search: {end_time - start_time} seconds")
print("Program by Animesh")
