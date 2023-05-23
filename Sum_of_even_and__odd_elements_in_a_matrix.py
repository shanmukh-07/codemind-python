r,c = map(int,input().split())
m = []
e,o=0,0
for i in range(r):
    x = list(map(int,input().split()))
    m.append(x)
for i in range(r):
    for j in range(c):
        if m[i][j]%2==0:
            e+=m[i][j]
        else:
            o+=m[i][j]
print(e,o)