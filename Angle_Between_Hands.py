def fun(c,d):
    c_a = 0.5*(60*c+d)
    d_a = 6*d
    a = abs(c_a-d_a)
    return min(a,360-a)


n = input()
a = n[:2]
b = n[3:]
c = int(a)   #time in hours
d = int(b)   #time in minutes

print(fun(c,d))