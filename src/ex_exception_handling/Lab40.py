# class SalaryNotInRangeError(Exception):
#
#     def __init__(self, salary, message="Salary is not in (5000,15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)
#
# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)

# class SalaryNotInRangeError(Exception):
#
#     def __init__(self, salary, message = "Salary is not in (5000,15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f'{self.salary} -> {self.message}'
#
# salary = int(input("Enter the salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError