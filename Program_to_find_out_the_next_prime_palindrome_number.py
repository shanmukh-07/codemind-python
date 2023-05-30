def fun1(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def fun2(n):
    a = str(n)
    if a == a[::-1]:
        return True
    return False

n = int(input())
a = n+1
while 1:
    if fun1(a) and fun2(a):
        print(a)
        break
    a+=1