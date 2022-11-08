n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    c1=a/b
    c2=a/c
    c3=a/(b*c)
    if c1>=d or c2>=d or c3>=d:
        print("Win")
    else:
        print("Lose")