def fun(a,b):
    l1 = list(a)
    l2 = list(b)
    for i in l1:
        if i in l2:
            l2.remove(i)
        else:
            return False
    return True

a,b = map(str,input().split())
print(fun(a,b))