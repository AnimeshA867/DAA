def quickSort(arr, l, r):
    if l < r:
        m = partition(arr, l, r)
        quickSort(arr, l, m - 1)
        quickSort(arr, m + 1, r)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, l, r):
    pivot = arr[r]  # Use the last element as pivot
    i = l - 1

    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, r)
    return i + 1

def main():
    arr = [52, 32, 10, 2, 41, 52, 36, 41]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)

if __name__ == "__main__":
    main()
