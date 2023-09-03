for _ in range(int(input())):
    a,b = map(int,input().split())
    c = 0
    for i in range(b):
        if (i*i)%b == a:
            c = i
            break
        else:
            c = -1
    print(c)