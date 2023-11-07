# 07b - Regular Expressions

'''
.. - match any two of any character
a|b - one a OR one b
(a|b)(a|b) - aa OR bb OR ab OR ba
(a|b)? - nothing OR a OR b
(a|b)* - nothing OR a OR b OR aa OR ab OR ba OR bb OR .... (any # of as or bs, including zero)
(a|b)+ - any number of as or bs, not including zero
(0|1|2){3} - exactly 3 characters, which are 0s, 1s, or 2s
[012]{3} - exactly 3 characters, which are 0s, 1s, or 2s
[0-2]{3} - exactly 3 characters, which are 0s, 1s, or 2s
[012]{3,5} - between 3 and 5 characters, which are 0s, 1s, or 2s
[012]{3,} - 3 or more characters, which are 0s, 1s, or 2s
(a|b|c|d|e|f|...) - any single lowercase letter
[abcdefghijklmnopqrstuvwxyz] - any single lowercase letter
[a-z] - any single lowercase letter
[a-z0-9] - any single lowercase letter or any single digit character
[-.,;:!?] - any single punctuation character
[^a-z] - any single character that isn't a lowercase letter
^ - just a single ^ character
\w+ - 1 or more lowercase letters OR uppercase letters OR digits OR an underscore
'''

import re 

ab_regex = re.compile('a|b')
# ab_match = ab_regex.match('a is a letter') # match() looks for a match at the start of the string
ab_match = ab_regex.search('Recognize some letter: a is my string') # search() looks for a match anywhere
print(f'{ab_match = }')
if ab_match:
    print(f'{ab_match.start() = }')
    print(f'{ab_match.end() = }')
    print(f'{ab_match.group() = }')
else:
    print('No match found')

email_regex = re.compile(r'^[a-z]+@[a-z]+\.[a-z]+$') # $ - end the string, ^ - start of string
# r - raw string (i.e. don't process any backslached characters)
email_match = email_regex.search('rfortier@ontarotechu.ca.com')
if email_match:
    print(f'{email_match.start() = }')
    print(f'{email_match.end() = }')
    print(f'{email_match.group() = }')
else:
    print('No match found')

name_re = re.compile('[A-Z][a-z]*')
print('All names: ', name_re.findall('John Jonah Jameson'))

price_re = re.compile(r'\d+(\.\d{2})?')
print('All prices: ', price_re.findall('The sale price of $199 is not worth it, but I got it for $49.99 which was a great deal.'))

