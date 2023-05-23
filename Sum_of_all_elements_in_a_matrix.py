r,c = map(int,input().split())
m = []
s=0
for i in range(r):
    x = list(map(int,input().split()))
    m.append(x)
    s+=sum(x)
print(s)