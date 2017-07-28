## This is a class without Modules



class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

emp1.first = "john"
emp1.last = "doe"
emp1.pay = "50000"

emp2.first = "sally"
emp2.last = "smith"
emp2.pay = "60000"



print(" ")

print(emp1.first + " " + emp1.last)
print(emp1)
print(dir(emp1))
print (" ")
print(emp1.__dict__)
print(" ")
print(vars(emp1))

print(" ")
print(emp2.first + " " + emp2.last)
print(dir(emp2))
print (" ")
print(emp2.__dict__)
print(" ")
print(vars(emp2))