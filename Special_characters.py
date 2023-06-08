n = input()
l1,l2,l3 =[],[],[]
for i in n:
    if not i.isdigit() and not i.isalpha():
        l1.append(i)
    elif i.isdigit() and int(i)%2==0:
        l2.append(i)
    elif i.isdigit() and int(i)%2!=0:
        l3.append(i)
a = len(l1)
l = []
while 1:
    if a%2 == 0:
        if len(l2) == 0 and len(l3) == 0:
            break
        elif len(l2) == 0:
            l.append(l3[0])
            l3.pop(0)
        elif len(l3) == 0:
            l.append(l2[0])
            l2.pop(0)
        else:
            l.append(l2[0])
            l.append(l3[0])
            l2.pop(0)
            l3.pop(0)
    else:
        if len(l2) == 0 and len(l3) == 0:
            break
        elif len(l2) == 0:
            l.append(l3[0])
            l3.pop(0)
        elif len(l3) == 0:
            l.append(l2[0])
            l2.pop(0)
        else:
            l.append(l3[0])
            l.append(l2[0])
            l3.pop(0)
            l2.pop(0)
        
z = "".join(l)
print(z)