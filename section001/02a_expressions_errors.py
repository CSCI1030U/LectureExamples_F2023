# 02a - expressions and errors

result = 7 * (4 + (3.1 / 2))
print(f'{result = }')
print(f'{type(result) = }')

print(f'{True  and True = }')
print(f'{True  and False = }')
print(f'{False and True = }')
print(f'{False and False = }')

print(f'{True  or True = }')
print(f'{True  or False = }')
print(f'{False or True = }')
print(f'{False or False = }')

cs = 'CSCI'
code = '1030U'
print(f'{cs + code = }')

code_num = 1030
print(f'{cs + str(code_num) = }')

# greeting = 'hi' + 'hi'
greeting = 'hi' * 2
print(f'{greeting = }')

print('-' * 50)

# errors

# syntax errors

# print('hello'  # syntax error:  '(' was never closed
# print('hello

x = 0
# if x < 10
#     print('x is small')

# runtime errors

course = 'CSCI1030U'
# print(f'{course[10] = }') # string index out of range

# quiz_count = 0
# quiz_mark_sum = 9 + 11 + 10
# print(f'{quiz_mark_sum / quiz_count = }') # division by zero

# logic errors

quiz_count = 2
print(f'{quiz_count = }')
quiz_mark_sum = 9 + 11 + 10
print(f'{quiz_mark_sum = }')
print(f'{quiz_mark_sum / quiz_count = }') # logic error
