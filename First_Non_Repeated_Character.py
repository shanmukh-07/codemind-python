for _ in range(int(input())):
    n = int(input())
    s = input()
    for i in range(n):
        if s.count(s[i]) == 1:
            print(s[i])
            break
    else:
        print(-1)