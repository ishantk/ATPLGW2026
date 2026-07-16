# Decorator : Design Pattern

class Burger:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print('{name} | {price}'.format_map(vars(self)))


# Decorator Design Pattern
class MealDecorator:

    def __init__(self, burger):
        self.burger = burger
        self.burger.price += 100

    def show(self):
        self.burger.show()
        print('Burger Upgraded to Meal with Fries and Coke')
    

burger1 = Burger(name='Mc Veggie', price=150)
# burger1.show()

meal = MealDecorator(burger=burger1)
meal.show()