# 04b - Functions

# Coding Exercise 04b.1

def get_class_average(marks):
    '''
    Calculates the statistical mean of `marks`.

    @param marks a list of floating point numbers

    @return the mean of `marks`. 
    '''
    return sum(marks) / len(marks)

avg = get_class_average([10.0, 11.0, 9.0])
print(f'{avg = }')
