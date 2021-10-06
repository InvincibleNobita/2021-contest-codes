t=int(input())
while t:
    n,k = map(int,input().split())
    nl=list(map(int,input().split()))
    
    nl.sort(reverse=True)
    nl=nl[:(2*k)+1]
    #print(nl)
    f,s=0,nl.pop()
    #print(s,nl)
    for i in range(len(nl)):
        if i%2==0:
            f+=nl[i]
        else:
            s+=nl[i]
    #print(f,s)
    print(max(f,s))
    
    
    
    t-=1
