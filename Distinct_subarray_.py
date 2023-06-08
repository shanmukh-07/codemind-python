l = int(input())
r = int(input())
m = []
for i in range(l,r+1):
    m.append(i)
l1 = []
for i in range(len(m)):
    for j in range(i,len(m)):
        c = m[i:j+1]
        l1.append(c)
c = 0
for i in l1:
    k = sum(i)
    if k%2!=0:
        c+=1
print(c)