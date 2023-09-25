# Coding Challenge 03a.1

import math

estimate = 0
num_reps = 50
x = math.pi / 2
adding = True 

for n in range(1, num_reps, 2):
    term = x ** n / math.factorial(n)

    if adding:        
        estimate += term 
    else:
        estimate -= term 

    adding = not adding 

print(f'{estimate = }')