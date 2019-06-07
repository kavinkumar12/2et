inp1=list(map(str,input()))
inp2=list(map(str,input()))
for i in range(0,len(inp2)):
   k=w=l=0
   w=ord(inp1[i])
   l=ord(inp2[i])
   k=w+l
   if k>96 and k<123:
        print(chr(k),end=" ")
    elif (k-96)<122 and(k-96)>96:
        k=k-96
        print(chr(k),end=" ")
    elif k>148:
        k=k-96-26
        print(chr(k), end=" ")
    else:
        k=k-26
        print(chr(k),end=" ")
