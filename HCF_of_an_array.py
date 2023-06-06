def fun1(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def fun2(arr):
    if len(arr) == 0:
        return None
    res = arr[0]
    for i in range(1,len(arr)):
        res = fun1(res , arr[i])
    return res


n = int(input())
arr = list(map(int,input().split()))
print(fun2(arr))