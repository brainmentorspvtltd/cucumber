class Employee:
    """Class Employee for creating new employee object"""
    id = None
    name = None
    dept = None
    salary = None
    company = "TPDDL"

ram = Employee()
ram.id = 101
ram.name = "Ram"
# ram.dept = "IT"
ram.salary = 45000
print(ram.__dict__)

shyam = Employee()
shyam.id = 102
shyam.name = "Shyam"
shyam.dept = "IT"
shyam.salary = 40000
shyam.company = "BMPL"
print(shyam.__dict__)