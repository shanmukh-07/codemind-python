n = int(input())
arr = list(map(int,input().split()))
s = sum(arr)
for i in range(n,-1,-1):
    if s%i == 0:
        print(i)
        break