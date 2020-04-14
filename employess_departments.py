class Company:
    def __init__(self, name, address, company_type):
        self.name = name
        self.address = address
        self.company_type = company_type
        self.employees = list()


class Employee:
    def __init__(self, name, department, start_date):
        self.name = name
        self.department = department
        self.start_date = start_date

company1 = Company("Wal-Mart", "123 Street", "retail")
company2 = Company("Goldman Sachs", "Money Street", "Investment")

employee1 = Employee('Jim', 'toys', 10/12/19)
employee2 = Employee('Tim', 'shoes', 10/12/19)
employee3 = Employee('Sam', 'accounting', 10/12/19)
employee4 = Employee('Pam', 'HR', 10/12/19)
employee5 = Employee('Michael', 'sales', 10/12/19)

company1.employees.append(employee1)
company1.employees.append(employee2)
company2.employees.append(employee3)
company2.employees.append(employee4)
company2.employees.append(employee5)

print(f'''{company1.name} is in the {company1.company_type} and has the following employees
        * {employee1.name}
        * {employee2.name}''')
print(f'''{company2.name} is in the {company2.company_type} and has the following employees
        * {employee3.name}
        * {employee4.name}
        * {employee5.name}''')
