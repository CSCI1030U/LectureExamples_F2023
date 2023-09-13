first_name = 'Randy'
last_name = 'Fortier'
full_name = first_name + last_name 

print(f'{full_name = }')
print(f'{first_name + last_name = }')

course_code = 1030
cs = 'CSCI'
# print(f'{cs + course_code = }') # runtime error, mismatched types
print(f'{cs + str(course_code) = }')

greeting = 'hi'
print(f'{greeting * 5 = }')
print("-"*50)

# errors

# syntax error
x = 0
# if x < 10    # syntax error:  expected ':'
#     print('x is a small number')

# print('Hello") # syntax error
# print('Hello' # syntax errors

# runtime errors
course = 'CSCI1030U'
print(f'{course[2] = }')
# print(f'{course[20] = }') # runtime error 'string index out of range'

count = 0
mark_sum = 21 + 19 + 20

print(f'{count = }')
# print(f'{mark_sum / count = }') # runtime error

count = 2
mark_sum = 21 + 19 + 20
print(f'{mark_sum / count = }') # logic error
