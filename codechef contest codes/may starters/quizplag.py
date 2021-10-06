#TLE
'''

t=int(input())
while t:
  n,m,k=map(int,input().split())
  kl=list(map(int,input().split()))
  cnt,done,ans=0,[],[]
  #print(cnt,done,ans)
  for i in range(k):
    if(kl[i]<=n):
      if kl[i] not in done:
        done.append(kl[i])
      else:
        if kl[i] not in ans:
          cnt+=1
          ans.append(kl[i])
  ans.sort()
  print(cnt,*ans,sep=' ')
  t-=1
    
'''


   


t=int(input())
while t:
  n,m,k=map(int,input().split())
  kl=list(map(int,input().split()))
  cnt=0
  vis=[0]*(n+1)
  ans=[]
  #print(cnt,done,ans)
  for i in range(k):
    if(kl[i]<=n):
      if vis[kl[i]]==0:
        vis[kl[i]]+=1
      elif vis[kl[i]]==1:
        vis[kl[i]]+=1
        cnt+=1
        ans.append(kl[i])
  ans.sort()
  print(cnt,*ans,sep=' ')
   
   
  t-=1

