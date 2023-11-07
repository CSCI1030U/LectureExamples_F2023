# 07b - Regular Expressions

'''
... - any 3 characters
.{3} - any 3 characters
.* - 0 or more of any character
m* - 0 or more 'm's
m+ - 1 or more 'm's
mm+ - 2 or more 'm's
m{2,} - 2 or more 'm's
m{3,5} - 3, 4, or 5 'm's
ab? - an 'a', followed by an optional 'b'
(ab)? - either an empty string or 'ab'
(ab)+ - 1 or more sequences of 'ab'
a|b - either an 'a' or a 'b'
(a|b)+ - 1 or more 'a's or 'b's
0|1|2|3|4|5|6|7|8|9 - any 1 digit character
[0123456789] - any 1 digit character
[0-9] - any 1 digit character
\d - any 1 digit character
[^0-9] - any 1 non-digit character
(a{3})|(b[01]+) - either 'aaa' or a 'b' then any 1 or more binary digits (0 or 1)
'''

import re 

xy_regex = re.compile('x|y')
# xy_match = xy_regex.match('The letter x is my least favourite letter')
xy_match = xy_regex.search('The letter x is my least favourite letter')
print(f'{xy_match = }')
if xy_match:
    print(f'{xy_match.start() = }')
    print(f'{xy_match.end() = }')
    print(f'{xy_match.group() = }')
else:
    print('No match found')

variable_regex = re.compile('^[a-zA-Z_]\w*$')
variable_match = variable_regex.search('min')
print(f'{variable_match = }')

name_re = re.compile('[A-Z][a-z]*')
print('All names: ', name_re.findall('John Jonah Jameson'))

price_re = re.compile(r'\d+(\.\d{2})?')
print('All prices: ', price_re.findall('The sale price of $199 is not worth it, but I got it for $49.99 which was a great deal.'))

