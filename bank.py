class Bank:
    def __init__(self, name):
        self.business_name = name
        self.customers = list()

first_tennessee = Bank("First Tennessee")


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

Joe = Customer("Joe", "Leland")
Blake = Customer("Blake", "Blue")
Sam = Customer("Dean", "Martin")

first_tennessee.customers.append(Joe)
first_tennessee.customers.append(Blake)
first_tennessee.customers.append(Sam)


for customer in first_tennessee.customers:
    print(f'{customer.first_name} {customer.last_name} is a customer at {first_tennessee.business_name}.')