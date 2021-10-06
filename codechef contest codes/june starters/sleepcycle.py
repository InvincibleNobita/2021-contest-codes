
t=int(input())
while t:
    l,h=map(int,input().split())
    s=input()
    ft=[]
    cnt=0
    for i in range(l):
        if(s[i]=='0'):
            cnt+=1
        else:
            ft.append(cnt)
            cnt=0
    ft.append(cnt)
    ft.sort(reverse=True)
    #print(ft)
    flag=False
    if(sum(ft)>0):
        i=0
        while i<len(ft):
            if(ft[i]!=0):
                if(ft[i]>=h):
                    flag=True
                    break
                else:
                    h=2*(h-ft[i])
            else:
                break
            i+=1
    if(flag):
        print("YES")
    else:
        print("NO")
    
    
    
    t-=1


