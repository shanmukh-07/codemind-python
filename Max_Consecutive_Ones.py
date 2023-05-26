n = int(input())
m = list(map(str,input().split()))
z = ''.join(m)
a = z.split('0')
l = [len(i) for i in a]
print(max(l))