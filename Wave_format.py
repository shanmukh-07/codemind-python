n = int(input())
arr = list(map(int,input().split()))
a = sorted(arr)
l = []
while 1:
    if len(a) == 1:
        l.append(a[0])
        break
    else:
        l.append(a[-2])
        l.append(a[-1])
        a.pop(-2)
        a.pop(-1)
    if len(a) == 0:
        break
print(*l)