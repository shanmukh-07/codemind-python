from itertools import permutations
s = input()
ns = [''.join(i) for i in permutations(s)]
for i in ns:
    print(i)