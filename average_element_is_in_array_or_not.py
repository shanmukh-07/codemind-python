n=int(input())
x=list(map(int,input().split()))
a=sum(x)//n
if a in x:
    print("True")
else:
    print("False")