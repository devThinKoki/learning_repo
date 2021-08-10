class CoffeeMachine:
    def __init__(self):
        """Class CoffeeMachine prints all the process of making coffee"""

    def start(self):
        print("Starting to make a coffee")
    
    def grinding(self):
        print("Grinding coffee beans")
    
    def boiling(self):
        print("Boiling water")
    
    def mixing(self):
        print("Mixing boiled water with crushed coffee beans")
        
    def pour_coffee(self):
        print("Pouring coffee into the cup")
        
    def pour_milk(self):
        print("Pouring some milk into the cup")
        
    def coffee_ready(self):
        print("Coffee is ready!")


coffee_machine = CoffeeMachine()

coffee_machine.start()
coffee_machine.grinding()
coffee_machine.boiling()
coffee_machine.mixing()
coffee_machine.pour_coffee()
coffee_machine.pour_milk()
coffee_machine.coffee_ready()