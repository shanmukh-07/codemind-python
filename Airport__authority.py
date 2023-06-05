l = []
for _ in range(int(input())):
    n = int(input())
    l.append(n)
m = int(input())
c = 0
for i in l:
    if i>m:
        c+=2
    else:
        c+=1
print(c)