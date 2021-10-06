t=int(input())
while t:
    n,m=map(int,input().split())
    nl=list(map(int,input().split()))
    ml=list(map(int,input().split()))
    cntf,cntr=[100000]*(n),[100000]*(n)
    cnt=[-1]*(n)
    
    #print(cnt,nl,ml)
    for i in range(1,n):
        
        if(cntf[i-1]<10000):
            cntf[i]=cntf[i-1]+1
        if(nl[i-1]==1):
            #print("l")
            cntf[i]=1
    nl.reverse()
    for i in range(1,n-1):
        if(cntr[i-1]<100000):
            cntr[i]=cntr[i-1]+1
        if(nl[i-1]==2):
            #print("r")
            cntr[i]=1
    cntr.reverse()
    cntf[0],cntr[0],cnt[0]=0,0,0
    #print(cntf,cntr)
    for i in range(1,n):
        cnt[i]=min(cntf[i],cntr[i])
        if(cnt[i]>=100000):
            cnt[i]=-1

        
            
            
    
    
    #print(cnt)
    i=0
    while i<m:
        print(cnt[ml[i]-1],end=' ')
        i+=1
    print()
        
        
    



    t-=1

