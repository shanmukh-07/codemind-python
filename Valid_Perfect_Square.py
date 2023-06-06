def fun(n):
    if n**0.5 == int(n**0.5):
        return True
    return False
    
for _ in range(int(input())):
    n = int(input())
    if fun(n):
        print("True")
    else:
        print("False")