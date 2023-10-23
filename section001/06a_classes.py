# 06a - Object-Oriented Programming I (Classes)

class Monitor:
    # refresh rate
    # diagonal_screen_size
    # connector type
    def __init__(self, refresh_rate=120, diagonal_screen_size=21.2, connector='HDMI'):
        self.__refresh_rate = refresh_rate
        self.__diagonal_screen_size = diagonal_screen_size
        self.__connector = connector

    # accessor / getter
    def get_refresh_rate(self):
        return self.__refresh_rate
    
    # mutator / setter
    def set_refresh_rate(self, new_refresh_rate):
        self.__refresh_rate = new_refresh_rate
    
    # used to convert to string by str()
    def __str__(self):
        return f'{self.__diagonal_screen_size}" monitor with {self.__refresh_rate} Mhz refresh rate'

    # overloaded operators
    def __lt__(self, other_monitor):
        return self.__refresh_rate < other_monitor.__refresh_rate
    
monitor1 = Monitor(240, 26.1, 'HDMI')
# monitor1.__refresh_rate = 144
monitor1.set_refresh_rate(144)
monitor1_str = str(monitor1)
print(monitor1_str)

monitor2 = Monitor(240, 26.1, 'HDMI')
print(f'{monitor1 < monitor2 = }')

print(f'{monitor2}')

# Coding Exercise 06a.1

class Cat:
    def __init__(self, name, mass):
        self.__name = name 
        self.__mass = mass 

    def get_name(self):
        return self.__name 
    
    def set_name(self, name):
        self.__name = name 
    
    def __str__(self):
        return f'{self.__name} ({self.__mass} kg)'
    
    def __lt__(self, other_cat):
        return self.__mass < other_cat.__mass
    
lenny = Cat('Lenny', 11.5)
print(f'{lenny.get_name() = }')
print(f'{str(lenny) = }')

boots = Cat('Boots', 7.4)
print(f'{boots < lenny = }')
