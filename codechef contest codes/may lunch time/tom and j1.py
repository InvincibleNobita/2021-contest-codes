
t=int(input())
while t:
    a,b,c,d,k=map(int,input().split())
    steps=(c-a)+(d-b)
    #print(c-a,d-b)
    #print(steps)
    if(steps<=k):
        if((steps%2==0) and (k%2==0)) or ((steps%2!=0) and (k%2!=0)):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")



    t-=1
