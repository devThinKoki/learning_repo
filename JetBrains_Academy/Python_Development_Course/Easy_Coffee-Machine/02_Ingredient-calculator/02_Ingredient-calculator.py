class CoffeeMachine:
    def __init__(self):
        """Class CoffeeMachine prints all the process of making coffee"""
        self.coffee_n = 0
        self.water_per_coffee = 200
        self.milk_per_coffee = 50
        self.beans_per_coffee = 15

    def calculate_ingredients(self):
        coffee_needs = input("Write how many cups of coffee you will need:\n")
        self.coffee_n = int(coffee_needs)
        print(f"""For {self.coffee_n} cups of coffee you will need:
{self.coffee_n * self.water_per_coffee} ml of water
{self.coffee_n * self.milk_per_coffee} ml of milk
{self.coffee_n * self.beans_per_coffee} g of coffee beans
For 125 cups of coffee you will need:
25000 ml of water
6250 ml of milk
1875 g of coffee beans""")

    # def start(self):
    #     print("Starting to make a coffee")
    
    # def grinding(self):
    #     print("Grinding coffee beans")
    
    # def boiling(self):
    #     print("Boiling water")
    
    # def mixing(self):
    #     print("Mixing boiled water with crushed coffee beans")
        
    # def pour_coffee(self):
    #     print("Pouring coffee into the cup")
        
    # def pour_milk(self):
    #     print("Pouring some milk into the cup")
        
    # def coffee_ready(self):
    #     print("Coffee is ready!")


coffee_machine = CoffeeMachine()
coffee_machine.calculate_ingredients()
# coffee_machine.start()
# coffee_machine.grinding()
# coffee_machine.boiling()
# coffee_machine.mixing()
# coffee_machine.pour_coffee()
# coffee_machine.pour_milk()
# coffee_machine.coffee_ready()