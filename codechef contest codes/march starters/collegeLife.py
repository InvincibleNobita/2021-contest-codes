def swaps(f,c):
    ans=[]
    i,j=0,0
    while (i<len(f) and j<len(c)):
        if(f[i]<c[j]):
            ans.append('f')
            i+=1
        elif(c[j]<f[i]):
            ans.append('c')
            j+=1
    while(i<len(f)):
        ans.append('f')
        i+=1
    while(j<len(c)):
        ans.append('c')
        j+=1
    
    return ans

t=int(input())
while t:
    n,m=map(int,input().split())
    nl=list(map(int,input().split()))
    ml=list(map(int,input().split()))
    res=swaps(nl,ml)
    #print(res)
    cnt=0
    if res[0]=='c':
        cnt=1
    for i in range(1,len(res)):
        if(res[i]!=res[i-1]):
            cnt+=1
    print(cnt)      

    t-=1
