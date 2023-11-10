# 08b - Exceptions and Testing

# Coding Exercise 08b.1

def print_reciprocals(n):
    for i in range(n, -1, -1):
        try:
            print(f'{1/i}')
        except ZeroDivisionError as error:
            # don't hide your error, let whoever needs to know, know about it
            print(f'Error while computing 1/n: {error}')

print_reciprocals(5)

# Coding Challenge 08b.1
class TooYoungToVote(Exception):
    pass

age = int(input('How old are you? '))
if age < 18:
    raise TooYoungToVote('You need to be 18 or older to vote, sorry!')


