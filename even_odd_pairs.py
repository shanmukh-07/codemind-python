n = int(input())
arr = list(map(int,input().split()))
l1,l2 = [],[]
for i in arr:
    if i%2 == 0:
        l1.append(i)
    else:
        l2.append(i)
l = []
while 1:
    if len(l1) == 0 and len(l2) == 0:
        break
    elif len(l1) == 0:
        l.append(l2[0])
        l2.pop(0)
    elif len(l2) == 0:
        l.append(l1[0])
        l1.pop(0)
    else:
        l.append(l1[0])
        l.append(l2[0])
        l1.pop(0)
        l2.pop(0)
if len(l)%2!=0:
    l.append(0)
print(*l)