def bubbleSort(arr):
    length=len(arr);

    print(arr);
    for i in range (0,length):
        for j in range (0,length-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;

        print(arr);


bubbleSort([2,7,4,1,5,3])