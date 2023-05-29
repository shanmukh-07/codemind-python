n = input()
s1 = 'aeiouAEIOU'
s2 = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
i = 0
j = len(n)-1
l = []
while i<j:
    if (n[i] in s1 and n[j] in s2) or (n[i] in s2 and n[j] in s1):
        l.append((n[i],n[j]))
    i+=1
    j-=1
print(len(l))