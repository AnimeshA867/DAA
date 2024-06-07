#Iteratively
def minmax(arr):
    max= arr[0]
    min=arr[0]
    for i in range (0,len(arr)):
        if arr[i]>max:
            max=arr[i]
        if arr[i]<min:
            min=arr[i]
    return max,min


#Divide and Conquer
from typing import List, Tuple

def minmax_dc(arr: List[int], l: int, r: int) -> Tuple[int, int]:
    """ 
    This function finds the minimum and maximum elements in the array using a divide and conquer approach.
    
    :param arr: List of integers
    :param l: Starting index of the array
    :param r: Ending index of the array
    :return: A tuple containing the minimum and maximum elements from the array
    """
    if l == r:
        return (arr[l], arr[l])
    elif l == r - 1:
        if arr[l] < arr[r]:
            return (arr[l], arr[r])
        else:
            return (arr[r], arr[l])
    else:
        mid = (l + r) // 2
        min1, max1 = minmax_dc(arr, l, mid)
        min2, max2 = minmax_dc(arr, mid + 1, r)

        min_final = min(min1, min2)
        max_final = max(max1, max2)

        return (min_final, max_final)

def main():
    arr = [25, 57, 48, 37, 12, 92, 36, 33]
    min_val, max_val = minmax_dc(arr, 0, len(arr) - 1)
    print(f"Minimum value in the array: {min_val}")
    print(f"Maximum value in the array: {max_val}")

if __name__ == "__main__":
    main()