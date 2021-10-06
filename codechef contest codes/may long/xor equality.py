def power(a,b,m) :
    res = 1
    if a == 0:
        return 0
 
    while b > 0:
        if ((b & 1) == 1) :
            #print('bodd=',b)
            res = (res * a) % m
            #print('res=',res)
        #print('beven=',b)
        b = b >> 1
        #print('b/2=',b)
        a = (a * a) % m
        #print('a=',a)
         
    return res
    
    
        
 
t=int(input())
while t:
    n=int(input())
    mod=(10**9)+7
    #ans=(((2**n)//2))%mod
    #print(ans)
    ans=power(2,n-1,mod)
    print(ans)
        
        
    



    t-=1

