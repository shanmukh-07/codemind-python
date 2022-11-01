n=int(input())
x=list(map(int,input().split()))
even=[]
odd=[]
for i in range(len(x)):
    if i%2==0:
        even.append(x[i])
    if i%2!=0:
        odd.append(x[i])
print(sum(even)-sum(odd))