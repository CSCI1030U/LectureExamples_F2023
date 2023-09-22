# 03b - Strings and Lists

full_name = 'Carla Rodriguez'
first = ''
last = ''
first_name_done = False 

for char in full_name:
    if char == ' ':
        first_name_done = True 
    
    elif not first_name_done:
        # this character is part of the first name
        # first = first + char 
        first += char

    else: 
        # this character is part of the last name
        last += char 

print(f'"{first}","{last}"')

# Coding Exercise 03b.2

marks = [10.0, 7.5, 8.0, 7.0, 8.25]
mark_sum = 0.0
for mark in marks:
    mark_sum += mark 

print(f'{mark_sum/len(marks) = }')
print(f'{sum(marks) / len(marks) = }')

# hacker's corner

squares = []
for n in range(100):
    squares.append(n ** 2)

squares2 = [n ** 2 for n in range(100)]

print(f'{squares = }')
print(f'{squares2 = }')