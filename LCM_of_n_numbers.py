import math
def fun(a,b):
    return abs(a*b)//math.gcd(a,b)
    
def fun2(arr):
    if len(arr) == 0:
        return None
    res = arr[0]
    for i in range(1, len(arr)):
        res = fun(res,arr[i])
    return res

n = int(input())
arr = list(map(int,input().split()))
print(fun2(arr))