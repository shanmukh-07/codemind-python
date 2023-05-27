r,c = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(r)]
l = []
for i in m:
    s=sum(i)
    l.append(s)
print(max(l))