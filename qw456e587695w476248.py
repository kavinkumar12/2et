a=int(input())
b=1000
for i in range(0,20):
    if pow(2,i)<=a:
        x = abs(pow(2, i) - a)
        if x < b: b = x
print(b)
