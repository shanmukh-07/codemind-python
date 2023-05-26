n = int(input())
arr = list(map(int,input().split()))
k = int(input())
a = max(arr)
for i in arr:
    if (i+k)>=a:
        print("True",end = ' ')
    else:
        print("False",end = ' ')
    