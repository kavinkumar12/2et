
from itertools import combinations
a,b=map(int,input().split())
s=len(str(a))
L=list(combinations(str(a),s-b))
L=(sorted(L))
D=" ".join(L[0])
print(D)
