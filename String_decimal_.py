for _ in range(int(input())):
    n = input()
    c = 0
    l = [i for i in n]
    for i in l:
        if i.isdigit():
            c+=1
    if c == len(n):
        print('True')
    else:
        print('False')