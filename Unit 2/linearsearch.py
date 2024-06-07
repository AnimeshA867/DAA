def linearSearch(arr,key):
    length =len(arr);
    flag=0
    for i in range (0,length):
        if(key==arr[i]):
            flag=1
    result = 'The value was %s found' % ('' if flag else 'not')
    print(result);


linearSearch(["Ram","Shyam","55","46"],"Computer");
linearSearch(["Ram","Shyam","55","46"],"Ram");
