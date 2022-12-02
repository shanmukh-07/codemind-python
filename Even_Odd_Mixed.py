n=int(input())
e=0
o=0
m=0
while n:
    if (n%10)%2==0:
        e+=1
    elif (n%10)%2:
        o+=1
    m+=1
    n//=10
if m==e:
    print("Even")
elif m==o:
    print("Odd")
else:
    print("Mixed")