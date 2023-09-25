# 03b - Strings and Lists

# Coding Exercise 03b.1

full_name = 'Carla Rodriguez'
first = ''
last = ''
first_name_done = False

for char in full_name:
    # three cases:
    # 1. encounter the space (first name is done, first -> last)
    # 2. encounter a non-space -> first
    # 3. encounter a non-space -> last
    if char == ' ':
        first_name_done = True 
    
    elif not first_name_done:
        # character is part of the first name
        # first = first + char
        first += char 

    else:
        # character is part of the last name 
        last += char 

print(f'"{first}","{last}"')

# lists

nums = [0,2,4,6,4,8]
nums.remove(4) # removes the first 4
print(f'{nums = }')

# Coding Exercise 03b.2

marks = [9.0, 10.0]
mark_sum = 0.0
for mark in marks:
    mark_sum += mark 
print(f'{mark_sum / len(marks) = }')
print(f'{sum(marks) / len(marks) = }')
