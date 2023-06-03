n = input()
n = n.lower()
a = n.count('z')
b = n.count('o')
if 2*a == b:
    print("Yes")
else:
    print("No")