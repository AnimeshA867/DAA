import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Input array
arr = [64, 34, 25, 12, 22, 11, 90]

# Measure the time taken to execute the Bubble Sort function
start_time = time.time()
bubble_sort(arr)
end_time = time.time()

# Output the result and time taken
print("Sorted array is:", arr)
print(f"Time taken to sort the array using Bubble Sort: {end_time - start_time} seconds")
print("Program by Animesh")
