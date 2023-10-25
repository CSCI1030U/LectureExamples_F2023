# 06b - Inheritance

# Coding Exercise 06b.1

class Pet:
    def __init__(self, name, breed, mass, sex):
        self._name = name 
        self._breed = breed 
        self._mass = mass 
        self._sex = sex 

class Dog(Pet):
    def speak(self):
        print(f'{self._name}: Woof!')

class Cat(Pet):
    def speak(self):
        print(f'{self._name}: Meow!')

pets = [
    Dog('Indi', 'Hound', 28.0, 'female'),
    Cat('Garfield', 'Long Hair', 12.0, 'male'),
]
for pet in pets:
    pet.speak() # polymorphic function call (determined using dynamic binding)

# Coding Exercise 06b.2
class Product:
    def __init__(self, price, description):
        self._price = price 
        self._description = description

class Shoe(Product):
    def __init__(self, price, description, brand, size, colour):
        super().__init__(price, description)
        self._brand = brand 
        self._size = size 
        self._colour = colour 
    
    def __str__(self):
        return f'{self._brand} (size: {self._size}, price: {self._price})'

shoe1 = Shoe(49.99, 'High heel with strappy thing', 'Jacques Morneau', 6.5, 'Silver')
shoe2 = Shoe(99.99, 'Pointy dress shoe', 'Jacques Morneau', 10.5, 'Black')
print(f'{str(shoe1) = }')
print(f'{str(shoe2) = }')
