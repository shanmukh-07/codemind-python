def fun(n):
    if n == n[::-1]:
        return True
    return False
    
for _ in range(int(input())):
    s = input()
    if not fun(s):
        print('NO')
    if fun(s) and len(s)%2 == 0:
        print('YES EVEN')
    if fun(s) and len(s)%2 != 0:
        print('YES ODD')