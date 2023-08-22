for _ in range(int(input())):
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    l,l1 = [],[]
    for i in range(a):
        for j in range(i,a):
            if sum(arr[i:j+1]) == b:
                l.append((i+1,j+1))
                l1.append(arr[i:j+1])
    if len(l1) == 0:
        print(-1)
    else:
        v = l[0]
        print(*v)