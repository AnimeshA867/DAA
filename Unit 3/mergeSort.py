""" def mergeSort(arr,l,r):
    arr2=[]
    if(l<r):
        m=int((l+r)/2)
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,arr2,l,m+1,r)
        
        
def merge(arr1, arr2, l, m, r):
    x = l
    y = m
    k = l
    while x < m and y < r:
        if arr1[x] <= arr1[y]:
            arr2[k] = arr1[x]
            x += 1
        else:
            arr2[k] = arr1[y]
            y += 1
        k += 1
    while x < m:
        arr2[k] = arr1[x]
        x += 1
        k += 1
    while y < r:
        arr2[k] = arr1[y]
        y += 1
        k += 1
    for i in range(l, r):
        arr1[i] = arr2[i]
      """   
        
        
def mergeSort(arr,l,r):
  
    
    if(l>=r):
        return;
    
    m=int((l+r)/2)
    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);
    merge(arr,l,m+1,r);
    
    
def merge(arr,l,m,r):
    arr2=[]*(r-l)
    x=l;
    y=m;
    k=x;
    
    while x<m and y<r:
        if(arr[x]<=arr[y]):
            arr2[k]=arr[x];
            x+=1;
        else:
            arr2[k]=arr[y];
            y+=1;
        
        k+=1;
    
    while x<m:
        arr2[k]=arr[x];
        x+=1;
        k+=1;
        
    while y<r:
        arr2[k]=arr[y];
        y+=1;
        k+=1;
        
    for i in range(l,r):
        arr[i]=arr2[i];
        

def main():
    arr=[25,57,48,37,12,92,36,33]
    mergeSort(arr,0,len(arr))
    print(arr)
    
if __name__=="__main__":
    main()