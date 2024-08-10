for _ in range(int(input())):
    a,b = map(int,input().split())
    s = input()
    while b:
        ss = s[:b]
        ss = ss[::-1]
        s = ss + s[b:]
        b -= 1
    print(s)