def binarySearch(arr, key, left, right):
    middle = int((left + right) / 2)
    
    if arr[middle] == key:
      
        return True
    
    if left > right:
        return False
    
    if arr[middle] < key:
        return binarySearch(arr, key, middle + 1, right)
    elif arr[middle] > key:
        return binarySearch(arr, key, left, middle - 1)

def main():
    found = binarySearch([10, 20, 30], 10, 0, 2)
   
    if found == True:
        print("The key has been found.")
    else:
        print("The key was not found.")

if __name__ == "__main__":
    main()
