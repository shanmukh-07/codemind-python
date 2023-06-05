for _ in range(int(input())):
    m = int(input())
    arr = list(map(int,input().split()))
    l = []
    while 1:
        if len(arr) == 1:
            l.append(arr[0])
            break
        else:
            l.append(arr[-1])
            l.append(arr[0])
            arr.pop(-1)
            arr.pop(0)
        if len(arr) == 0:
            break
    print(*l)