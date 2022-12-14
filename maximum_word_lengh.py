n=list(map(str,input().split()))
b=''
for i in n:
    if len(i)>len(b):
        b=i
print(len(b))