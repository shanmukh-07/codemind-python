def fun(n):
    s = 0
    m = str(n)
    for i in m:
        s+=int(i)**2
    return s

n = int(input())
while True:
    n = fun(n)
    if len(str(n)) == 1 and (n == 1 or n == 7):
        print("True")
        break
    if len(str(n)) == 1 and (n!=1 or n!=7):
        print("False")
        break