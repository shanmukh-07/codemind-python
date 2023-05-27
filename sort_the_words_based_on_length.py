n = input()    # 'tokyo palermo rio nairobi professor denver'
m = n.split()  # ['tokyo', 'palermo', 'rio', ' nairobi', 'professor', 'denver']
m.sort()       # ['denver','nairobi', 'palermo', 'professor', 'rio' ,'tokyo']
m.sort(key=len)# ['rio','tokyo','denver','nairobi', 'palermo','professor']
z = ' '.join(m)
print(z)