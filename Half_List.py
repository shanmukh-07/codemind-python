n=int(input())
arr=list(map(int,input().split()))
a=n/2
b=n/2
s1=[]
s2=[]
s3=[]
arr2=arr[::-1]
for i in arr:
    s1.append(i)
    a=a-1
    if a==0:
        break
for i in arr2:
    s2.append(i)
    b=b-1
    if b==0:
        break
s3=s2+s1
for i in s3:
    print(i,end=' ')