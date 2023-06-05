a,b=map(int,input().split())
x = list(map(int,input().split()))
c=abs(a-b)
a1=x[:-c]
a2=x[-c:]
for i in a1:
    a2.append(i)
print(*a2)