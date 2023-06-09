s = input()
l = list(s)
l1,l2,l3 = [],[],[]
for i in range(len(l)):
    for j in range(i,len(l)):
        c = l[i:j+1]
        l1.append(c)
for i in l1:
    count = 0
    ns = 'aeiou'
    for j in i:
        if j in ns:
            count+=1
    if count == len(i):
        l3.append(count)
print(max(l3))