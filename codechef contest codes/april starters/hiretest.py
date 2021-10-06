from collections import Counter

t=int(input())
while t:
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    while n:
        m=input()
        m=Counter(m)
        xl=m['F']
        yl=m['P']
        if(x<=xl or (x-1<=xl and y<=yl)):
            print(1,end='')
        else:
            print(0,end='')
        


        n-=1
    print()


    t-=1
