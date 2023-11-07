# 07b - Regular Expressions

'''
.. - any two characters
x|y - one x or one y
(x|y)(x|y) - two characters, each of which is x or y
(x|y)* - 0 or more characters, each of which is x or y
(x|y)+ - 1 or more characters, each of which is x or y
(x+|y+) - 1 or more xs or 1 or more ys
a?b - an optional a, then a b
(x|y){2,6} - 2 to 6 characters, each of which is x or y
(a|b|c|d|e|f|...) - any single lowercase letter
[abcdefghijklmnopqrstuvwxyz] - any single lowercase letter
[a-z] - any single lowercase letter
[a-zA-Z] - any letter (lowercase or uppercase)
\w+ - a word character (uppercase, lowercase, digit, or underscore), 1+ times
[.,;:!?] - any single punctuation character
\w+\.\w+ - 1+ word characters, then a period, then 1+ word characters
([01][01])+ - a binary number with an even number of digits
'''
import re 

xy_regex = re.compile('x|y')
xy_result1 = xy_regex.match('x with some stuff after')
print(f'{xy_result1 = }')
if xy_result1:
    print(f'Match starts at index {xy_result1.start() = }')
    print(f'Match ends at index {xy_result1.end() = }')
    print(f'The string matched was {xy_result1.group() = }')
else:
    print('No match found')
xy_result2 = xy_regex.search('can we find the x in this string?')
print(f'{xy_result2 = }')
xy_result3 = xy_regex.match('some stuff before, then an x with some stuff after')
print(f'{xy_result3 = }')

phone_num = '905-721-8668' # also: '721-8668'
# ^ - the start of the string
# $ - the end of the string
phone_regex = re.compile('^(\d{3}-)?[0-9]{3}-\d{4}$')
phone_result = phone_regex.match(phone_num)
if phone_result:
    print(f'Valid phone # found: {phone_result.group()}')
else:
    print('Not a valid phone #')

name_re = re.compile('[A-Z][a-z]*')
print('All names: ', name_re.findall('John Jonah Jameson'))

price_re = re.compile(r'\d+(\.\d{2})?')
print('All prices: ', price_re.findall('The sale price of $199 is not worth it, but I got it for $49.99 which was a great deal.'))
