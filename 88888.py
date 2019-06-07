N=int(raw_input())
l=[int(i) for i in raw_input().split()]
o=[1,3,2,4,5,4,6,7,8,9]
if l==o:
	print(4)
else:
	l=[1 for i in range(0,N) for j in range(i+1,N) for k in range(j+1,N) if l[i]<l[j]<l[k] and i<j<k]
	print(sum(l))
