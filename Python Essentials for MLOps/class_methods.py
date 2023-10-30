# def build_profile(**user_info):
#     for key, value in user_info.items():
#         print(f"{key}: {value}")
#
# build_profile(first_name="John", last_name="Doe", age=30)  # Arbitrary keyword arguments
# # output
# first_name: John
# last_name: Doe
# age: 30
# -----------------------------------------------------------
# class Budget:
#     def __init__(self, budget):
#         self.budget = budget  # self is used to represent the instance of a class.
#
#     def expenses(self, amount):
#         self.budget = self.budget - amount
#         self.report() # use self to call method inside class
#
#     def report(self):
#         print(f"budget is : {self.budget}")
#
#
# fiscal_budget = Budget(100)
# print(fiscal_budget.expenses(50))
# print((fiscal_budget.budget))
# --------------------------------------------------------------------

# class inheritance

class Pet:  # parent class

    def eat(self):
        self.food = self.food - self.appetite
        print(f"Ate {self.appetite} of food, have {self.food} left")


class Parakeet(Pet):  # child class
    def __init__(self):
        self.food = 100
        self.appetite = 5


class Dog(Pet):
    def __init__(self):
        self.food = 100
        self.appetite = 77


perry = Parakeet()  # Parakeet class [extends Pet]
rufus = Dog()

perry.eat()
rufus.eat()
# -------------------------------
import unittest


class Testing(unittest.TestCase): # inherted TestCase in Testing class
    pass


test = Testing()

for attribute in dir(test):
    if attribute.startswith('_'):
        continue
    print(attribute)
