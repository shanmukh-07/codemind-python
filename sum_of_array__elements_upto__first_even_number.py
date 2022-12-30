n=int(input())
arr=list(map(int,input().split()))
s=[]
for i in arr:
    if i%2==0:
        break
    s.append(i)
print(sum(s))