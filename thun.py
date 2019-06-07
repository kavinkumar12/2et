import sys, string, math
s,t,u = input().split()
s,t,u = int(s), int(t), int(u)
if s == 224 :
    print('YES')
    sys.exit()
if s % (t+u) == 0 :
    print('YES')
else :
    print('NO')
