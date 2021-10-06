
t=int(input())
while t:
  n,k,f=map(int,input().split())
  nn=n
  s,e=[],[]
  while n:
    sl,el=map(int, input().split())
    s.append(sl)
    e.append(el)

    n-=1
  #print(s,e)

  time=s[0]
  for i in range(1,nn):
      diff=s[i]-e[i-1]
      print(diff)
      if diff>=0:          
          time+=diff
          print('pos')
      else:
          print('old',e[i])
          if e[i]<e[i-1]:
              print('change')
              e[i]=e[i-1]
          
          print('new',e[i])
  time+=(f-e[-1])
  print('t',time,k)
  if time>= k:
      print("YES")
  else:
      print("NO")
       


  t-=1
