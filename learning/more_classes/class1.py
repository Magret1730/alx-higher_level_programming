class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # to take the class as first argument rather than instance as first argument
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp_1 = Employee('Coree', 'Schaffer', 50000)
emp_2 = Employee('Oyedele', 'Faith', 60000)

# Employee.set_raise_amt(10)  # same as Employee.raise_amt = 10 and emp_1.set_raise_amt(10)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

emp_str_1 = 'Faith-Sanjo-70000'
emp_str_2 = 'Sarah-Labake-80000'
emp_str_3 = 'Grace-Dayo-50000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)
