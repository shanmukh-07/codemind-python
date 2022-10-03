N=int(input())
z=len(str(N))
y=0

for i in range(z):
    if(N%10>y):
        y=N%10
        N=N//10
    else:
        N=N//10
print(y)