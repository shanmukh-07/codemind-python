def fun(n):
    s = ''   # C
    while n>0:  # 159 -> 6
        r = n%26 # 3 -> 6
        if r == 0:
            s += 'Z'
            n = (n//26) - 1
        else:
            s += chr(r-1+ord('A'))  #chr(3-1+65) -> chr(67) -> C #
            n = n//26
    return s[::-1]
n = int(input())
print(fun(n))