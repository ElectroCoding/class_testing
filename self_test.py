## Note - you can print or use the "self" object 
## inside a Module because the "self" parameter is 
## passed in when the Module is called.
## The "self" object cannot be used outside the Module.


class Employee:

    def __init__(self):
        print(id(self))


emp1 = Employee()
emp2 = Employee()

print(emp1)
print(dir(emp1))
print (" ")
print(emp1.__dict__)
print(" ")
print(vars(emp1))
