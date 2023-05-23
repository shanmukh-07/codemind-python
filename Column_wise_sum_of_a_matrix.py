r,c = map(int,input().split())
m = []
for i in range(r):
    x = list(map(int,input().split()))
    m.append(x)
for j in range(c):
    s=0
    for i in range(r):
        s+=m[i][j]
    print(s,end = ' ')