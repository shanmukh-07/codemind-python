def adddigits(num):
    sum=0
    while num:
        d=num%10
        num=num//10
        sum=sum+d
    return sum

n=int(input())
while n>9:
    n=adddigits(n)
print(n)