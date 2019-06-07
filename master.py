from itertools import combinations
b,a=map(int,input().split())
s=len(str(b))
L=list(combinations(str(b),s-a))
L=(sorted(L))
D="".join(L[0])
print(D)
