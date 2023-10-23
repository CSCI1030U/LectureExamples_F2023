# 06a - Object-Oriented Programming I (Classes)

class GPU:
    # price
    # memory
    # number of cores
    # clock speed 
    def __init__(self, price, memory, num_cores, clock_speed):
        self.set_price(price)
        self.memory = memory 
        self.num_cores = num_cores 
        self.clock_speed = clock_speed 

    # mutator / setter
    def set_price(self, price):
        self.price = price

    # accessor / getter
    def get_price(self):
        return self.price    

    def get_rating(self):
        if self.num_cores < 250:
            return 1
        elif self.num_cores < 500:
            return 3
        else:
            return 5
        
    def __str__(self):
        return f'GPU with {self.memory} memory, and {self.num_cores} cores.'
    
    def __lt__(self, other):
        return self.get_rating() < other.get_rating()

rtx4090 = GPU(449.99, '16 GB', 675, '2.8 GHz')
print(f'{rtx4090.get_rating() = }')
rtx4090_str = str(rtx4090)
print(f'{rtx4090_str = }')
rtx3070 = GPU(199.99, '12 GB', 340, '2.2 GHz')
print(f'{rtx3070 < rtx4090 = }')
