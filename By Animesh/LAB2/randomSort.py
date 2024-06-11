import time
import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# Input array
arr = [3, 6, 8, 10, 1, 2, 1]

# Measure the time taken to execute the Randomized Quick Sort function
start_time = time.time()
randomized_quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()

# Output the result and time taken
print("Sorted array is:", arr)
print(f"Time taken to sort the array using Randomized Quick Sort: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
