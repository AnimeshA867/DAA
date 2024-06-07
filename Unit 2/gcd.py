def gcd(m,n):

    while n!=0 or m!=0 :
        if(m==0):
            return n;

        
        elif(n==0):
            return m;

        else:
            r=m%n;
            m=n;
            n=r;
    

gcdValue=gcd(24,9);
print('The value of gcd is ',gcdValue);
