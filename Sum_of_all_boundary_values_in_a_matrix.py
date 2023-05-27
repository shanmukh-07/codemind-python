r,c = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(r)]
s = 0
for i in range(r):
    for j in range(c):
        if i==0:
            s+=m[i][j]
        elif j == 0:
            s+=m[i][j]
        elif i == c-1:
            s+=m[i][j]
        elif j == r-1:
            s+=m[i][j]
print(s)