import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Input array
arr = [3, 6, 8, 10, 1, 2, 1]

# Measure the time taken to execute the Quick Sort function
start_time = time.time()
sorted_arr = quick_sort(arr)
end_time = time.time()

# Output the result and time taken
print("Sorted array is:", sorted_arr)
print(f"Time taken to sort the array using Quick Sort: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
