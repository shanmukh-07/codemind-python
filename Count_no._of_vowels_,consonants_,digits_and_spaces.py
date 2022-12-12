n=input()
vc=0
cc=0
dc=0
sc=0
for i in n:
    if i==chr(32):
        sc+=1
    elif i.isdigit():
        dc+=1
    elif i==chr(97) or i==chr(65) or i==chr(101) or i==chr(69) or i==chr(105) or i==chr(73) or i==chr(111) or i==chr(79) or i==chr(117) or i==chr(85):
        vc+=1
    else:
        cc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",dc)
print("White spaces:",sc)
    