n = int(input())
l = ['A','B','C','D','E','F','G','H','I','J']
for i in range(n):
    for j in range(i,n):
        print(l[n-i-1],end = ' ')
    print()