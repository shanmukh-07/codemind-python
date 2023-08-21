def fun(n,arr):
    m = -1 # 1
    for i in range(n-1,-1,-1):
        t = arr[i] # t = 1 6
        arr[i] = m # -1 1
        m = max(m,t) # 1 6
    return arr
n = int(input())
arr = list(map(int,input().split()))
a = fun(n,arr)
print(*a)