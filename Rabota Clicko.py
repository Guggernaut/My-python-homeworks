class Company:
    def __init__(self, company_name, company_bank):
        self.company_name = company_name
        self.company_bank = company_bank

class Person(Company):
    def __init__(self, company_name, company_bank, first_name, last_name, salary):
        super().__init__(company_name, company_bank)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

def get_salary(self):
    if self.company_bank < self.salary:
        print("У компании недостаточно средств")
    else:
        self.company_bank -= self.salary
        print(f'Остаток капитала компании {self.company_bank}')

def get_info(self):
    print(f"Информация о сотруднике: {self.first_name}{self.last_name} зарплата: {self.salary}\n")

bank = Person('Ne Skam Bank', 10000, 'Vladimir', 'Clicko', 40000)

get_info(bank)
get_salary(bank)

