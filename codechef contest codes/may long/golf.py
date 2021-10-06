from math import gcd

t=int(input())
while t:
    k=int(input())
    cnt=0
    for i in range(1,(2*k)+1):
        f=k+ (i*i)
        #print(f)
        s=k+ ((i+1)*(i+1))
        #print(s)
        cnt+=gcd(f,s)
        #print(cnt)
    
    print(cnt)
    
        
    



    t-=1
