# 06a - Object-Oriented Programming I (Classes)

class Student:
    def __init__(self, student_num, age, name):
        self.set_student_num(student_num)
        self.__age = age # private variable
        self.name = name
        self.gpa = 0.0
        print('__init__ called')
        
    # getter / accessor
    def get_student_num(self):
        return self.student_num 
    
    # setter / mutator
    def set_student_num(self, new_student_num):
        self.student_num = new_student_num
        print('set_student_num called')
    
    def encourage(self, message):
        print(f'{self.name}: {message}')

    def __str__(self):
        return f'{self.name} ({self.student_num})'
    
    def __lt__(self, other):
        return self.gpa < other.gpa

shaela1 = Student(100000001, 18, 'Shaela')
shaela2 = Student(100000001, 18, 'Shaela')
# print(f'{shaela.__age = }') # can't access private variable
shaela_str = str(shaela1)
print(f'{shaela_str = }')
print(f'{shaela1 < shaela2 = }')

# Coding Exercise 06a.1

class Cat:
    def __init__(self, name, mass):
        self.__name = name 
        self.__mass = mass 

    def __str__(self):
        return f'{self.__name} weighs {self.__mass}kg'
    
    def __lt__(self, other_cat):
        return self.__mass < other_cat.__mass
    
lenny = Cat('Lenny', 5.0)
print(f'{str(lenny) = }')

boots = Cat('Boots', 4.2)
print(f'{str(boots) = }')
print(f'{lenny < boots = }')
