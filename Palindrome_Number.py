def palin(n):
    n=str(n)
    if n==n[::-1]:
        return True
    else:
        return False
for i in range(int(input())):
    x=int(input())
    if palin(x):
        print("True")
    else:
        print("False")