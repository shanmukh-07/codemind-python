s = input()
hr = int(s[:2])
mn = int(s[3:])
hr = hr%12
mn_ang = 6*mn
hr_ang = 30*hr + 0.5*mn
ang = abs(hr_ang-mn_ang)
print(min(ang,360-ang))
# print(mn_ang,hr_ang)