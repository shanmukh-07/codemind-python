r,c = map(int,input().split())
m = []
a=[]
for i in range(r):
    x = list(map(int,input().split()))
    m.append(x)
for i in m:
    a.append(sum(i))
print(sum(a))