"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    
    def __init__(self, name, contract_type, wage_or_salary, commission_type = None, commission_rate = None, hours_worked = None, contracts_landed = None):
        self.name = name
        self.contract_type = contract_type
        self.wage_or_salary = wage_or_salary
        self.commission_type = commission_type
        self.commission_rate = commission_rate
        self.hours_worked = hours_worked
        self.contracts_landed = contracts_landed
        self.commission_pay = 0
        self.commission_exp = " "

    def get_pay(self):
        
        if self.contract_type == "Salary":
            contract_pay = self.wage_or_salary
            
        elif self.contract_type == "Hourly":
            if self.hours_worked is None:
                raise ValueError("The number of hours worked must be provided for hourly employees.")
            
            contract_pay = self.wage_or_salary * self.hours_worked
            
        else:
            raise ValueError("Invalid contract type!")

        commission_pay = 0
        commission_exp = " "

        if self.commission_type == "Bonus":
            if self.commission_rate is None:
                raise ValueError("The commission rate must be provided for employees with a bonus commission.")
            
            self.commission_pay = self.commission_rate
            self.commission_exp = (f" and receives a bonus commission of {self.commission_rate},")
            
        elif self.commission_type == "Contract":
            if self.commission_rate is None or self.contracts_landed is None:
                raise ValueError("Commission rate and number of contracts landed must be provided for employees with a contract commission.")
            
            self.commission_pay = self.commission_rate * self.contracts_landed
            self.commission_exp = (f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_rate}/contract,")

        total_pay = contract_pay + self.commission_pay
        return total_pay

    def __str__(self):
        
        contract_exp = " "

        if self.contract_type == "Salary":
            contract_exp = (f"works on a monthly salary of {self.wage_or_salary},")

        elif self.contract_type == "Hourly":
            if self.hours_worked is None:
                raise ValueError("Hours worked must be provided for hourly employees.")
            
            contract_exp = (f"works on a contract of {self.hours_worked} hours at {self.wage_or_salary}/hour,")

        pay_exp = (f"their total pay is {self.get_pay()}.")
        return (f"{self.name} {contract_exp}{self.commission_exp} {pay_exp}")

billie = Employee('Billie', 'Salary', 4000)
charlie = Employee('Charlie', 'Hourly', 25, hours_worked = 100)
renee = Employee('Renee', 'Salary', 3000, 'Contract', 200, contracts_landed = 4)
jan = Employee('Jan', 'Hourly', 25, 'Contract', 220, hours_worked = 150, contracts_landed = 3)
robbie = Employee('Robbie', 'Salary', 2000, 'Bonus', 1500)
ariel = Employee('Ariel', 'Hourly', 30, 'Bonus', 600, hours_worked = 120)

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
