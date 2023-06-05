def fun(n,arr,m):
    if n>m:
        c = n-m
    else:
        c = m%n
        c = n-c
    d = arr[c:]
    e = arr[:c]
    l = []
    for i in d:
        l.append(i)
    for i in e:
        l.append(i)
    return l

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
a = fun(n,arr,m)
print(*a)