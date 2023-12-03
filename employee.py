"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    
    def __init__(self, name, contract_type, wage_or_salary, commission_type=None, commission_amount=None, hours_worked=None, contracts_landed=None):
        self.name = name
        self.contract_type = contract_type
        self.wage_or_salary = wage_or_salary
        self.commission_type = commission_type
        self.commission_amount = commission_amount
        self.hours_worked = hours_worked
        self.contracts_landed = contracts_landed

    def get_pay(self):
        if self.contract_type == "Salary":
            contract_pay = self.wage_or_salary
        elif self.contract_type == "Hourly":
            contract_pay = self.wage_or_salary * self.hours_worked
        else:
            raise ValueError("Invalid contract type!")

        commission_pay = 0
        if self.commission_type == "Bonus":
            commission_pay = self.commission_amount
        elif self.commission_type == "Contract":
            commission_pay = self.commission_amount * self.contracts_landed

        return contract_pay + commission_pay

    def __str__(self):
        contract_str = f"{self.name} works on a "
        if self.contract_type == "Salary":
            contract_str += f"monthly salary of {self.wage_or_salary} "
        elif self.contract_type == "Hourly":
            contract_str += f"contract of {self.hours_worked} hours at {self.wage_or_salary}/hour "

        commission_str = ""
        if self.commission_type == "Bonus":
            commission_str += f"and receives a bonus commission of {self.commission_amount}"
        elif self.commission_type == "Contract":
            commission_str += f"and receives a commission for {self.contracts_landed} contract(s) at {self.commission_amount}/contract"

        return f"{contract_str}{commission_str}. Their total pay is {self.get_pay()}."


billie = Employee('Billie', 'Salary', 4000)
charlie = Employee('Charlie', 'Hourly', 25, hours_worked=100)
renee = Employee('Renee', 'Salary', 3000, 'Contract', 200, contracts_landed=4)
jan = Employee('Jan', 'Hourly', 25, 'Contract', 220, hours_worked=150, contracts_landed=3)
robbie = Employee('Robbie', 'Salary', 2000, 'Bonus', 1500)
ariel = Employee('Ariel', 'Hourly', 30, 'Bonus', 600, hours_worked=120)

print(billie.get_pay())  
print(str(billie)) 

print(charlie.get_pay())  
print(str(charlie)) 

print(renee.get_pay())  
print(str(renee))

print(jan.get_pay())  
print(str(jan))  

print(robbie.get_pay()) 
print(str(robbie))  

print(ariel.get_pay())  
print(str(ariel))  
