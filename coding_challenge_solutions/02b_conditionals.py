# Coding Challenge 02b.1

# Write a program that asks the user for a single mark (out of 100), and outputs the letter grade that corresponds to that mark
# - Use the following ranges:
#   - 0-49: 	F
#   - 50-59: 	D
#   - 60-69: 	C
#   - 70-79: 	B
#   - 80-100: A

mark = int(input('Enter a mark (0-100): '))
if mark < 50.0:
    letter_grade = 'F'
elif mark < 60.0:
    letter_grade = 'D'
elif mark < 70.0:
    letter_grade = 'C'
elif mark < 80.0:
    letter_grade = 'B'
else:
    letter_grade = 'A'
print(f'{letter_grade = }')