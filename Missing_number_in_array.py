for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    l = []
    for i in range(1,n+1):
        l.append(i)
    for i in l:
        if i not in arr:
            print(i)