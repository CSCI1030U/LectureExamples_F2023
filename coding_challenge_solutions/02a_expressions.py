# Coding Challenge 02a.1

# Write a program that asks the user for a midterm mark, a lab mark, and a final exam mark and outputs the student's final mark (out of 100)
# - Midterm is out of 80, but has weight 30
# - Labs are out of 30, and has weight 30
# - Final exam is out of 180, but has weight 40

midterm_mark = int(input('Midterm mark: '))
lab_mark     = int(input('Lab mark:     '))
final_mark   = int(input('Final mark:   '))
mark = (midterm_mark / 80 * 30) + lab_mark + (final_mark / 180 * 40)
print(f'{mark = }')