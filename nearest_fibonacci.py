n = int(input())
a = 0
b = 1
while b<n:
    c = a+b
    a = b
    b = c
if abs(a-n) < abs(b-n):
    print(a)
elif abs(a-n) == abs(b-n):
    print(a,b)
else:
    print(b)