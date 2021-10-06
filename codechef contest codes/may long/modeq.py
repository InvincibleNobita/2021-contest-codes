
t=int(input())
while t:
    n,m=map(int,input().split())
    cnt=0
    for a in range(1,n):
        for b in range(1,n+1):
            if a<b:
                if ((m%a)%b)==((m%b)%a):
                    #print(m,'%',a,')%',b,'==',m,'%',b,')%',a)
                    cnt+=1
    print(cnt)
    
        
    



    t-=1
