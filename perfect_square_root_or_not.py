import math
n=int(input())
r=math.sqrt(n)
if int(r+0.5)**2==n:
    print("True")
else:
    print("False")