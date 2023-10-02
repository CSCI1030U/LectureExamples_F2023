# 04b - Functions
def add2(a,b):
    a = a + b
    return a

x,y = 1,2
print(f'{add2(x,y) = }') # passed by value
print(f'{x = },{y = }')

def add2_list(values):
    values[0] = values[0] + values[1]
    return values[0]

nums = [1,2]
print(f'{add2_list(nums) = }') # pass by reference
print(f'{nums[0] = },{nums[1] = }')

# Coding Exercise 04b.1

def get_class_average(marks):
    return sum(marks) / len(marks)

midterm_marks = [10.0, 11.0, 9.0]
print(f'{get_class_average(marks = midterm_marks) = }')

# float addOne(float &x) {
#     x += 1;
# }
