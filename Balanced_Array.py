for _ in range(int(input())):
    n = int(input())
    l = []
    arr = list(map(int,input().split()))
    for i in range(n):
        if sum(arr[:i]) == sum(arr[i+1:]):
            l.append(i)
    if len(l) > 0:
        print('YES')
    else:
        print('NO')