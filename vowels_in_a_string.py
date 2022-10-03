s=input()
c=0
ind=0
ch=input()
for char in s:
    if char==ch:
        print(True)
        ind=1
        print(s.index(char))
        break
if ind==0:
    print(False)