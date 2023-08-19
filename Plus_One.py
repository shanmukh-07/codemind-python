n = int(input())
arr = list(map(str,input().split()))
s = ''.join(arr)
ns = int(s)+1
l = [i for i in str(ns)]
print(*l)