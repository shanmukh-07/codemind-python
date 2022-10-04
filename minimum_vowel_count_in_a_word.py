s=list(map(str,input().split()))
t=999
for i in range(len(s)):
    c=0
    for char in s[i]:
        if char in 'aeiouAEIOU':
            c+=1
    if c<t:
        t=c
print(t)