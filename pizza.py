class Pizza():
    def __init__(self):
        self.size = ""
        self.style = ""
        self.crust = ""
        self.sauce = ""
        self.cheese = ""
        self.meat = ""
        self.veggies = ""

    def order_pizza(self, size, style, crust, sauce, cheese, meat, veggies):
        self.size = size
        self.style = style
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese 
        self.meat = meat
        self.veggies = veggies

    def order(self):
        print(f'You ordered a {self.size} pizza that is {self.style}, {self.crust} and has {self.sauce} sauce. For toppings you wanted {self.cheese} with {self.meat} and {self.veggies}')


pizza1 = Pizza()
pizza1.order_pizza('large', 'thin crust', 'buttered', 'marinara', 'mozzarella', 'pepperoni', 'mushroom')
pizza1.order()
pizza2 = Pizza()
pizza2.order_pizza('medium', 'deep dish', 'stuffed', 'white', 'cheddar', 'bacon', 'peppers')
pizza2.order()