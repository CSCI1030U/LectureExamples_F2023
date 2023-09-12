result = 7 * (3 + (3.1 / 2))
print(f'{result = }')
print(f'{type(result) = }')

cs = 'CSCI'
code = '1030U'

print(f'{cs + code = }')

# print(f'{cs * code = }')
print(f'{cs * 10 = }')
# print(f'{cs * 10.5 = }')

# errors

# syntax errors
# print('Hello world!") # syntax error
# 12 = x # syntax error

# runtime errors (exceptions)
# count = 0
# average_age = (20 + 21 + 19) / count // logic error
# print(f'{average_age = }')

# logic errors
count = 2
print(f'{count = }')
average_age = (20 + 19 + 21) / count
print(f'{len([19,21,20]) = }')

print(f'{average_age = }')
