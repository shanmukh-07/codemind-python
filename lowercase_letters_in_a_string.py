str=input()
sum=0
for char in str:
    k=char.islower()
    if k==True:
        sum+=1
print(sum)