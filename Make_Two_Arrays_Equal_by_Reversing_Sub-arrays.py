m = int(input())
arr1 = list(map(int,input().split()))
n = int(input())
arr2 = list(map(int,input().split()))
if sorted(arr1) == sorted(arr2):
    print('True')
else:
    print('False')