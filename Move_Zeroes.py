n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l[i]!=0:
        print(l[i],end=' ')
for j in range(n):
    if l[j]==0:
        print(l[j],end=' ')
        