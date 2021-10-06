t=int(input())
while t:
    x,y,xr,yr,d=map(int,input().split())
    val= min((x//xr),(y//yr))
    if(val>=d):
        print("YES")
    else:
        print("NO")


    
    t-=1
