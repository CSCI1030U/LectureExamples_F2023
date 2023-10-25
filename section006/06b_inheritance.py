# 06b - Inheritance

# Coding Exercise 06a.1
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

dog1 = Dog('Shams', 'Golden Retriever', 15.0, 'female')
cat1 = Cat('Sohrob', 'Long Hair Domestic', 7.0, 'female')
pets = [dog1, cat1]
for pet in pets:
    pet.speak()

# Coding Exercise 06a.2
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
        return f'{self._brand} (size: {self._size}, price: {self._price})'

shoe1 = Shoe('Georgina Ruffali', 6.5, 'Silver', 39.99, 'high heel with strappy thing')
shoe2 = Shoe('Louis Rouneau', 10.0, 'Black', 79.99, 'pointy dress shoe')
print(f'{str(shoe1) = }')
print(f'{str(shoe2) = }')
