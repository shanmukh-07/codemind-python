for _ in range(int(input())):
    s = input()
    l = list(s)
    nl = sorted(l)
    c = 0
    for i in range(len(nl)-1):
        if abs(int(nl[i])-int(nl[i+1])) == 1:
            c+=1
    if c == len(nl)-1:
        print("YES")
    else:
        print("NO")