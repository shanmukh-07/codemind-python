n = int(input())
arr = list(map(int,input().split()))
a = []
for i in arr:
    if i not in a:
        a.append(i)
for i in a:
    print(i,end=' ')