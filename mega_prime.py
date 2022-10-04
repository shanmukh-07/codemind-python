import math
def isprime(num):
    if num==1:
        return False
    sq=int(math.sqrt(num))
    for i in range(2,sq+1):
        if num%i==0:
            return False
    return True
num=int(input())
if isprime(num):
    while num:
        d=num%10
        num=num//10
        if not isprime(d):
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")