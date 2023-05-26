n = input()
s = n.split()
l = [] 
for i in s:
    l.append(list(i))
for i in l:
    print(min(i),max(i),end = ' ')