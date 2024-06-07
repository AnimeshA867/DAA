def insertionSort(arr):
    for i in range (1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        print(arr)    
    return arr

def main():
    arr = [25, 57, 48, 37, 12, 92, 36, 33]
    print(insertionSort(arr))
    
if __name__ == "__main__":
    main()
    
    