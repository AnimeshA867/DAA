import random

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, l, r):
    pivot = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1

def rand_partition(A, l, r):
    k = l + int((r - l) * random.random())
    swap(A, k, r)
    return partition(A, l, r)

def rand_quick_sort(A, l, r):
    if l < r:
        m = rand_partition(A, l, r)
        rand_quick_sort(A, l, m - 1)
        rand_quick_sort(A, m + 1, r)

def main():
    A = [10, 5, 2, 0, 7, 6, 4]
    print("Unsorted array:", A)
    rand_quick_sort(A, 0, len(A) - 1)
    print("Sorted array:  ", A)

if __name__ == "__main__":
    main()
