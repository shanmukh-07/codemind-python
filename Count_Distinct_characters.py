n = input()
a = n.lower()
l = [] 
for i in a:
    if i.isalpha():
        l.append(i)
b = set(l)
print(len(b))