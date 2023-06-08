m = input()
n = list(m)
i = 0
j = len(n) - 1
while i<j:
    if n[i].isalpha() and n[j].isalpha():
        n[i],n[j] = n[j],n[i]
        i+=1
        j-=1
    elif n[i].isalpha() and not n[j].isalpha():
        j-=1
    elif not n[i].isalpha() and n[j].isalpha():
        i+=1
    else:
        i+=1
        j-=1
b = "".join(n)
print(b)