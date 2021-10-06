from math import gcd
t=int(input())
while t:
    n=input()
    b=0
    for e in n:
        b+=int(e)
    print(n,b)
    ans=gcd(int(n),b)
    while ans==1:
        b=b+1
        ans=gcd(int(n),
        
        


    t-=1
