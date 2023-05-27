r,c = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(r)]
s = 0
for i in range(1,r-1):
    for j in range(1,c-1):
        s+=m[i][j]
print(s)