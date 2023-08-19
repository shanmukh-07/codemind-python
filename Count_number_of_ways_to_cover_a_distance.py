def fun(n):
    if n < 4:
        l = [1,2,4]
        return l[n-1]
    return fun(n-1) + fun(n-2) + fun(n-3)
n = int(input())
print(fun(n))