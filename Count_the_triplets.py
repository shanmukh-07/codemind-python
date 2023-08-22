for _ in range(int(input())):
    a = int(input())
    arr = list(map(int,input().split()))
    c = 0
    for i in range(a):
        for j in range(i+1,a):
            if (arr[i]+arr[j]) in arr:
                c+=1
    if c < 1:
        print(-1)
    else:
        print(c)