import math
import functools
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(k):
    a,b=map(int,input().split())
    t=functools.reduce(math.gcd,l[a-1:b])
    print(t)
