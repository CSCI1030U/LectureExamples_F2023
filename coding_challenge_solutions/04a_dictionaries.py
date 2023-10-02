# Coding Challenge 04a.1

names = ['first name', 'last name', 'favourite food']
values = ['Suresh', 'Abrar', 'Falafel Wrap']

person = {}
for i in range(len(names)):
    person[names[i]] = values[i]

print(f'{person = }')