n = input()
n = n.replace(' ','')
k = int(input())
a1 = k//len(n) 
a2 = k%len(n) 
c1 = (n.count('a'))*a1 
z = n[:a2] 
c2 = z.count('a') 
print(c1+c2)