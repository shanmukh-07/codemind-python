n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    if s==l:
        print("0")
    else:
        print(max(s)-min(s))
    