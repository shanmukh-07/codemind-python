def fun(n):
    c=1
    a=[i for i in range(1,n+1)]
    for i in a:
        c*=i
    return c
n=input()
a=list(n)
s=0
for i in a:
    i=int(i)
    s+=fun(i)
if s==int(n):
    print(f"The number {s} is a strong number")
else:
    print(f"The number {int(n)} is not a strong number")