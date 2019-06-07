u,v=map(str,input().split())
l1=0
if len(u)>len(v):
  u,v=v,u
i=0
while i<len(u):
  l1+=(ord(v[i])-ord(u[i]))
  i+=1
for i in range(i,len(v)):
  l1+=ord(v[i])-ord('a')+1
print(l1)
