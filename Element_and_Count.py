n = int(input())
arr = list(map(int,input().split()))
s=[]
l=[]
for i in arr:
    if i in s:
        pass
    else:
        a = arr.count(i)
        s.append(i)
        l.append(i)
        l.append(a)
print(*l)