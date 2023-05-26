n = input()
l = []
s = 'aeiou'
c = 0
for i in n:
    if i.isalpha():
        l.append(i)
b = set(l)
for i in s:
    if i in b:
        c+=1
if c == 5:
    print("True")
else:
    print("False")