# DRY - Donot Repeat Yourself

class Employee:
    """Class Employee for creating new employee object"""
    id = None
    name = None
    dept = None
    salary = None
    company = "TPDDL"

    def takeInput(self, id, name, dept, salary):
        self.id = id
        self.name = name
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(self.name, self.salary, self.dept)

ram = Employee()
# ram.id = 101
# ram.name = "Ram"
# ram.dept = "IT"
# ram.salary = 45000
# print(ram)
ram.takeInput(101,"Ram","IT",45000)
ram.showDetails()

shyam = Employee()
# shyam.id = 102
# shyam.name = "Shyam"
# shyam.dept = "IT"
# shyam.salary = 40000
# shyam.company = "BMPL"
# print(shyam.id, shyam.name, shyam.dept, shyam.salary)
shyam.takeInput(102,"Shyam","HR",46000)
shyam.showDetails()