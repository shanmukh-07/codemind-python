n=int(input())
lst=list(map(int,input().split()))
x=[i for i in lst if i%2==0]
print(sum(x))