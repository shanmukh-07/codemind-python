n=int(input())
arr=list(map(int,input().split()))
b=set(arr)
if len(b)==1:
    print(0)
else:
    m=0
    for i in range(n):
        c=0
        for j in range(1,n):
            if arr[i]==arr[j]:
                c+=1
                if m<c:
                    m=c
    print(m)
            