n = int(input())
for i in range(n):
    for j in range(n):
        if i == j or i == n-j-1:
            print('x',end = "")
        else:
            print('0',end = "")
    print()