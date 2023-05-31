def fun(a):
    if a<2:
        return False
    for i in range(2,a):
        if a%i == 0:
            return False
    return True
n = int(input())
b = str(n)
m = b[::-1]
c = int(m)
if fun(n) and fun(c):
    print("circular prime")
if (fun(n) and not fun(c)) or (not fun(n) and fun(c)):
    print("prime but not a circular prime")
if not fun(n) and not fun(c):
    print("not prime")