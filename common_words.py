s1 = input()
s2 = input()
s3 = s1.lower()
s4 = s2.lower()
s5 = s3.split()
s6 = s4.split()
l = []
for i in s6:
    if i in s5:
        l.append(i)
if len(l) == 0:
    print("-1")
else:
    print(*l)