for i in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    c = abs(n-k)
    a = arr[0:c]
    l = []
    for i in range(c,n):
        l.append(arr[i])
    for i in a:
        l.append(i)
    print(*l)