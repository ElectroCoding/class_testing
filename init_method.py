class Employee:

    def __init__(self, first, last, pay):
        self.first1 = first
        self.last1 = last
        self.pay1 = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        "{} {}".format(self.first, self.last)

emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Sally", "Smith", 60000)

print (emp1.email)
print (emp2.email)
print(vars(emp2))
print(emp2.last1)