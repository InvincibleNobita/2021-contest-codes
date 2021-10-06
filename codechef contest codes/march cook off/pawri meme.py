t=int(input())
while t:
    s=input()
    for j in range(len(s)-4):
        if s[j]=='p' and s[j+1]=='a' and s[j+2]=='r' and s[j+3]=='t' and s[j+4]=='y':
            s=s[:j]+'pawri'+s[j+5:]
    print(s)
        
        
    t-=1
