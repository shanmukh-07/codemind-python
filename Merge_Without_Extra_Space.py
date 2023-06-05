for _ in range(int(input())):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr3 = arr1+arr2
    a = sorted(arr3)
    print(*a)