import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input array
arr = [64, 25, 12, 22, 11]

# Measure the time taken to execute the Selection Sort function
start_time = time.time()
selection_sort(arr)
end_time = time.time()

# Output the result and time taken
print("Sorted array is:", arr)
print(f"Time taken to sort the array using Selection Sort: {end_time - start_time} seconds")
print("Program by Animesh")
