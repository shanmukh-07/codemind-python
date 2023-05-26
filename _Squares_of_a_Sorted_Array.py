n = int(input())
arr = list(map(int,input().split()))
l = [abs(i) for i in arr]
m = [i**2 for i in l]
m1 = sorted(m)
print(*m1)