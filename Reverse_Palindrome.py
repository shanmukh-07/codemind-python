def pal(n):
    r=0
    while n:
        a=n%10
        r=r*10+a
        n=n//10
    return r
n=int(input())
while n:
    a=pal(n)
    b=a+n
    if pal(b)==b:
        print(b)
        break
    n=b