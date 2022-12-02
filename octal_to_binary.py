o=int(input())
d=0
i=0
b=0
while o!=0:
    d=d+(o%10)*pow(8,i)
    i+=1
    o//=10
i=1
while d!=0:
    b=b+(d%2)*i
    d//=2
    i=i*10
print(b)