n = int(input())
arr = list(map(str,input().split()))
s=0
a=[]
for i in arr:
    s=len(i)
    a.append(s)
b=max(a)
for i in arr:
    if len(i)==b:
        print(i,end=' ')