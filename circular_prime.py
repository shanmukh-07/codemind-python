def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = input()
m = n[::-1]
a = int(n)
b = int(m)
if fun(a) and fun(b):
    print("circular prime")
if (fun(a) and not fun(b)) or (not fun(a) and fun(b)):
    print("prime but not a circular prime")
if not fun(a) and not fun(b):
    print("not prime")