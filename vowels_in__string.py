s="AEIOUaeiou"
v=input()
g=[]
for i in v:
    if i in s:
        if i not in g:
            g.append(i)
print(*g)