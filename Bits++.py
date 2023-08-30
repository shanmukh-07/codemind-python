c = 0
for _ in range(int(input())):
    n = input()
    if '++' in n:
        c+=1
    elif '--' in n:
        c-=1
print(c)