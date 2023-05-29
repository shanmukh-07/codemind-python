def fun(z):
    s1 = 'aeiouAEIOU'
    s2 = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    i=0
    j=len(z)-1
    l = []
    while i<j:
        if (z[i] in s1 and z[j] in s2) or (z[i] in s2 and z[j] in s1):
            l.append((z[i],z[j]))
        i+=1
        j-=1
    return len(l)

n = input()
m = n.split()
l1 = []
for i in m:
    z = fun(i)
    l1.append(z)
print(sum(l1))