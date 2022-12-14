n=list(map(str,input().split()))
b=n[0]
for i in n:
    if len(i)<=len(b):
        b=i
print(len(b))