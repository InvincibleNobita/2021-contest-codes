t=int(input())
z=1
while z<=t:
    g=int(input())
    ans=0
    for i in range(1,g+1):
      val= ((2*g)+i-(i*i))
      if (val%(2*i))==0 and val>0:
        #print(i)
        ans+=1
      




    print("Case #", z, ": ",ans,sep='')
    z+=1
