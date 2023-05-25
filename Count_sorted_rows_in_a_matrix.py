r,c = map(int,input().split())
m = []
c = 0
for i in range(r):
    x = list(map(int,input().split()))
    m.append(x)
for i in range(r):
    if m[i] == sorted(m[i]) or m[i] == sorted(m[i],reverse = True):
        c+=1
print(c)