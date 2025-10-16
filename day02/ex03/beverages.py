class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self):
        valeur = f"name : {self.name}\n"
        valeur += f"price : {self.price:0.2f}\n"
        valeur += f"description: {self.description()}\n"
        return valeur

class Coffee(HotBeverage):
    def __init__(self):
        self.price = 0.40
        self.name = "coffee"

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"

class Chocolate(HotBeverage):
    def __init__(self):
        self.price = 0.50
        self.name = "chocolate"

    def description(self):
        return  "Chocolate, sweet chocolate..."

class Cappucino(HotBeverage):
    def __init__(self):
        self.price = 0.45
        self.name = "cappucino"

    def description(self):
        return "Un po’ di Italia nella sua tazza!"