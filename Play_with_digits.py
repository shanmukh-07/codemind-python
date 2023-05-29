n = int(input())
arr = list(map(int,input().split()))
s = 0
for i in arr:
    i = str(i)
    for j in i:
        j = int(j)
        s+=j
print(s)