# 08b - Exceptions and Testing

# Coding Exercise 08b.1

def print_reciprocals(max_n):
    for n in range(max_n, -1, -1):
        try:
            print(f'{1/n}')
        except ZeroDivisionError as error:
            print(f'1/n is dividing by zero when n=0: {error}')
            

print_reciprocals(5)
print('after the call to print_reciprocals()')

# Coding Challenge 08b.1

class TooYoungToVoteError(Exception):
    pass

age = int(input('How old are you? '))
if age < 18:
    raise TooYoungToVoteError('You need to be 18 or older to vote')

