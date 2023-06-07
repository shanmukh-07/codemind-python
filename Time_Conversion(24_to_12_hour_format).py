n = input()
a = n[:2]
b = n[3:]
x = a
d = ''
if x == '24':
    x = '00'
elif x > '12':
    x = int(x) - 12
    x = str(x)
    if len(x) == 1:
        x = '0' + x
elif x == '00':
    x = '12'
else:
    x = a
    
if a>='00' and a<'12':
    d = 'AM'
else:
    d = 'PM'

print(f'{x}:{b} {d}')