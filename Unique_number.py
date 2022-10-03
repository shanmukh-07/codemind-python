def fun(d,num):
    while num:
        k=num%10
        num=num//10
        if d==k:
            return True
    return False
n=int(input())
sum=0
while n:
    d=n%10
    n=n//10
    if fun(d,sum):
        print("Not Unique Number")
        break
    sum=sum*10+d
else:
    print("Unique Number")