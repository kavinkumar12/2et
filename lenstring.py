b=input()
b=int(b)
K=[]
for i in range(0,b):  
    y=input()
    K.append(y)
D=[]
for i in zip(*K):
    if i.count(i[0])==len(i): 
        D.append(i[0])
    else:
        break
print(''.join(D))
