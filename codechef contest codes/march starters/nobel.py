t=int(input())
while t:
    n,m=map(int,input().split())
    nl=list(map(int,input().split()))
    ans={}
    flag=False
    for i in range(1,m+1):
        ans[i]=0
    #print(ans)
    for i in range(n):
        if ans[nl[i]]==0:
            ans[nl[i]]=1
    #print(ans)
    for i in ans.values():
        if i==0:
            flag=True
            break
    if(flag):
        print("YES")
    else:
        print("NO")


    t-=1
