

def check(lst):
    
    flag=True
    for i in range(len(lst)): 
      
      item=lst[i]
      if(item.islower()):
          for e in item:              
              if not(97<=ord(e)<=109):
                  flag=False
                  break
              
      elif(item.isupper()):
          for e in item:
              if not(78<=ord(e)<=90):
                  flag=False
                  break
            
      else:
          flag=False
    return flag

    

    
        


t=int(input())
while t:
  raw=list(map(str, input().split()))
  raw.reverse()
  k=int(raw.pop())
  fg=check(raw)
  if fg:
      print("YES")
  else:
      print("NO")
  
  



  t-=1
