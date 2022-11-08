n=input()
x=[]
for i in n:
    if i.isdigit():
        x.append(i)
s=len(x)
if s==0:
    print("Doesn't contain digit")
else:
    print("Contains %d digit"%s)