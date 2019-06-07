X,Y=input().split()
s=abs(len(X)-len(Y))
for i in range(len(X)):
    if len(Y)==1 and Y[i] in X:
        break
    if X[i]!=Y[i]:
        s=s+1
print(s)
