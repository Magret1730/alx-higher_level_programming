# Que: Take in a date and return whether it is work date or not
# This has nothing to do with any specific instance or class variable
# so we can use a static method for it
# To know if you're to use static method is when you dont need to access
# instance or class

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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Coree', 'Schaffer', 50000)
emp_2 = Employee('Oyedele', 'Faith', 60000)

import datetime
my_date = datetime.date(2023, 8, 6)

print(Employee.is_workday(my_date))
