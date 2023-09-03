s = input()
n = int(input())
a1 = n//len(s)
a2 = n%len(s)
c1 = s.count('a') * a1
z = s[:a2]
c2 = z.count('a')
print(c1+c2)