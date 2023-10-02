# 04b - Functions

# Coding Exercise 04b.1 

midterm_marks = [11.0, 9.0, 10.0]
def get_class_average(marks):
    '''
    Calculates the statistical mean of `marks`.
    '''
    # marks[0] = 0.0
    return sum(marks) / len(marks)

# pass by reference
print(f'{get_class_average(midterm_marks) = }')
print(f'{midterm_marks = }')

def add2(a, b):
    return a + b
    # a += b
    # return a 

x,y = 1,2
# pass by value
print(f'{add2(x,y) = }')
print(f'{x = },{y = }')
