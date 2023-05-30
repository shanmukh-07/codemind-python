n = input()
a = list(n)
for i in range(len(a)):
    if a[i] == '6':
        a[i] ='9'
        break
x = ''.join(a)
print(int(x))