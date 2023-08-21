def fun(arr):
    if not arr:
        return 0
    max_profit = 0
    m = arr[0]  # m = 7
    for i in arr:
        if i<m: #
            m = i
        else:
            max_profit = max(max_profit, i-m)
    return max_profit
n = int(input())
arr = list(map(int,input().split()))
print(fun(arr))