import random
from beverages import HotBeverage

class CoffeeMachine():
    def __init__(self):
        self.broken = 0
    
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.price = 0.90
            self.name = "empty cup"

        def description(self):
            return  "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self):
        self.broken = 0
    
    def serve(self, hot_beverage):
        if self.broken == 10:
            raise self.BrokenMachineException()
        i = random.randint(0, 1)
        self.broken += 1
        if i % 2 == 0:
            return self.EmptyCup()
        else:
            return hot_beverage