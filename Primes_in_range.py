def shan(v):
    for i in range(2,int(v**0.5)+1):
        if v%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
count=0
for v in range(a,b+1):
    if(shan(v) and v!=1):
        count+=1
print(count)