for _ in range(int(input())):
    a = input()
    b = input()
    c = a[0]
    d = b[0]
    c = 0
    for i in range(len(a)):
        if ord(a[i])-ord(b[i]) <= 0 :
            c+=1
    if c == len(a):
        print("YES")
    else:
        print("NO")