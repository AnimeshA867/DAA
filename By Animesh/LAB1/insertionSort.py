import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input array
arr = [12, 11, 13, 5, 6]

# Measure the time taken to execute the Insertion Sort function
start_time = time.time()
insertion_sort(arr)
end_time = time.time()

# Output the result and time taken
print("Sorted array is:", arr)
print(f"Time taken to sort the array using Insertion Sort: {end_time - start_time} seconds")
print("Program by Animesh")
