# 08b - Exceptions and Testing

# Coding Exercise 08b.1
def print_reciprocals(list):
    for n in list:
        try:
            print(f'{1/n}')
        except ZeroDivisionError as error:
            # TODO: handle this properly
            print(f'Dividing by zero when calculating 1/n')

print_reciprocals([5,4,3,2,1,0])
print('All done reciprocating')

# Coding Challenge 08b.1

class TooYoungToVoteError(Exception):
    pass

age = int(input('How old are you? '))
if age < 18:
    raise TooYoungToVoteError('You need to be 18 to vote')
