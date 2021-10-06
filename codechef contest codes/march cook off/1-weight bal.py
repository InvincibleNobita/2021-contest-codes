t=int(input())
while t:
    w1,w2,x1,x2,m=map(int,input().split())
    minw=w1+(x1*m)
    maxw=w1+(x2*m)
    if(minw<=w2<=maxw):
        #print(w1, minw, w2, maxw)
        print(1)
    else:
        print(0)
    t-=1
