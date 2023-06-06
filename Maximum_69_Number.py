n = input()
l = list(n)
for i in range(len(n)):
    if l[i] == '6':
        l[i] = '9'
        break
a = "".join(l)
print(a)