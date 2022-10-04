l=list(map(str,input().split()))
arr=[]
if len(l)==1:
    c=0
    for char in l[0]:
        if char in'aeiouAEIOU':
            c=1
    print(c)
else:
    for ch in l:
        c=0
        for char in ch:
            if char in 'aeiouAEIOU':
                c+=1
        arr.append(c)
    c=0
    for i in range(len(arr)):
        if arr[i]==min(arr):
            c+=1
    print(c)