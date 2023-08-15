n = int(input())
if n<3:
    print("The pattern is not possible")
else:
    for i in range(n):
        for j in range(n):
            if j<=i:
                print("*",end='')
        print()
    for i in range(1,n):
        for j in range(n):
            if i<=j:
                print("*",end='')
        print()