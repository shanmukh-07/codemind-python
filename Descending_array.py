m=int(input())
n=list(map(int,input().split()))
if sorted(n)==n[::-1]:
    print("yes")
else:
    print("no")