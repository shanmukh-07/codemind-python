n = input()
a = n.split()
b = []
for i in a:
    b.append(list(i))
for i in b:
    print(min(i),max(i),end = ' ')