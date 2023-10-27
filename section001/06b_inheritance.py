# 06b - Inheritance

# Coding Exercise 06b.1
class Pet:
    def __init__(self, name, breed, mass, sex):
        self._name = name 
        self._breed = breed 
        self._mass = mass 
        self._sex = sex 
    
    # def speak(self):
    #     return 'Error: cannot speak'

class Dog(Pet):
    def speak(self):
        print(f'{self._name}: Woof!')

class Cat(Pet):
    def speak(self):
        print(f'{self._name}: Meow!')

class Robot:
    def speak(self):
        print('Beep boop beep')

pets = [
    Dog('Keva', 'Sheepadoodle', 15.0, 'female'),
    Cat('Lenny', 'Long Hair Domestic', 9.2, 'male'),
    Robot(), # can't do this in Java
]
for pet in pets:
    pet.speak()

# Coding Exercise 06b.2

class Product:
    def __init__(self, price, description):
        self._price = price 
        self._description = description

class Shoe(Product):
    def __init__(self, brand, size, colour, price, description):
        super().__init__(price, description)
        self._brand = brand 
        self._size = size 
        self._colour = colour 
    
    def __str__(self):
        return f'{self._brand} (price: {self._price}, colour: {self._colour})'

products = [
    Shoe('Giovanna Barducci', 7.0, 'red', 39.99, 'high heel with strappy thing'),
    Shoe('Loic Montagne', 11.0, 'black', 99.99, 'pointy dress shoe'),
]
for product in products:
    print(str(product))