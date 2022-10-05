n=int(input())  
num_of_digits = len(str(n))  
square = n**2  
last_digits = square%pow(10,num_of_digits)  
if last_digits == n:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number")