def selectionSort(arr):
    n=len(arr);
    
    for i in range (0,n-1):
        min = i;
        for j in range (i+1,n):
            if(arr[j]<arr[min]):
                min = j;
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
        print(arr);
    return arr;

def main(): 
    arr = [25,57,48,37,12,92,36,33]
    print(selectionSort(arr));


if __name__ =="__main__":
    main();