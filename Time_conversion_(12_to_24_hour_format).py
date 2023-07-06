n = input()
if len(n)<8:
    n = '0' + n
a = n[6:]
b = n[:2]
c = n[2:5]
if a == 'AM' and b == '12':
    b = '00'
elif a == 'PM' and b == '12':
    b = '12'
elif a == 'PM':
    b = int(b)+12
    b = str(b)
print(f'{b}{c}')