def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = int(input())
a = n+1
b = n-1
while True:
    if fun(n):
        print(0)
        break
    elif fun(a) and fun(b):
       c = abs(a-n)
       d = abs(b-n)
       print(min(c,d))
       break
    elif fun(a):
       print(abs(n-a))
       break
    elif fun(b):
       print(abs(n-b))
       break
    else:
        a+=1
        b-=1