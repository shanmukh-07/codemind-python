n = int(input())
arr = list(map(int,input().split()))
s=[]
for i in arr:
    if i == arr.count(i):
        s.append(i)
a=set(s)
print(len(a))