a=int(input())
while a!=1:
    if a%5==0:
        a=a//5
    elif a%3==0:
        a=a//3
    elif a%2==0:
        a=a//2
    else:
        print("Not Ugly Number")
        break
else:
    print("Ugly Number")
        