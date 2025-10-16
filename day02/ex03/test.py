from beverages import HotBeverage, Coffee, Chocolate, Cappucino, Tea
import random
from machine import CoffeeMachine
beverages = []
beverages.append(HotBeverage())
beverages.append(Coffee())
beverages.append(Chocolate())
beverages.append(Cappucino())
beverages.append(Tea())

coffee_machine = CoffeeMachine()
try:
    for i in range(0, 20):
        j = random.randint(0, 4)
        print(coffee_machine.serve(beverages[j]))
except CoffeeMachine.BrokenMachineException as e:
    print(e)
coffee_machine.repair()
try:
    for i in range(0, 20):
        j = random.randint(0, 4)
        print(coffee_machine.serve(beverages[j]))
except CoffeeMachine.BrokenMachineException as e:
    print(e)