# 03b - Strings and Lists

# Coding Exercise 03b.1

full_name = 'Clint Eastwood'
first = ''
last = ''
first_name_done = False
for char in full_name:
    if char == ' ':
        first_name_done = True 
        # first_name_done = not first_name_done

    elif first_name_done:
        # this character is part of the last name
        last += char 
        # last = last + char 

    else: 
        # this character is part of the first name 
        first += char 

print(f'"{first}" "{last}"')
