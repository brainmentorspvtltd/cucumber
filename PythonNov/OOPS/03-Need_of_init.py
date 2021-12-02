class Employee:
    """Class Employee for creating new employee object"""
    company = "TPDDL"
    
    # Constructor
    def __init__(self, id, name, dept, salary):
        self.id = id
        self.name = name
        self.dept = dept
        self.salary = salary
        self.details = []
        self.details.append([self.id, self.name, self.dept, self.salary])

    def showDetails(self):
        # print(self.name, self.salary, self.dept)
        print(self.details)

ram = Employee(101,"Ram","IT",45000)
# ram.takeInput(101,"Ram","IT",45000)
ram.showDetails()

shyam = Employee(102,"Shyam","HR",46000)
# shyam.takeInput(102,"Shyam","HR",46000)
shyam.showDetails()

mac = Employee(103,"Mac","IT",50000)
# mac.takeInput(103,"Mac","IT",50000)
mac.showDetails()