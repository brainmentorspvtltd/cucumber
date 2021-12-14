class Employee:
    company = "TPDDL"

    def __init__(self, id, name, dept, salary):
        self.id = id
        self.name = name
        self.dept = dept
        self.salary = salary
        self.details = []
        self.details.append([self.id, self.name, self.dept, self.salary])

    def showDetails(self):
        print(self.details)

    def __del__(self):
        print(self.name, "deleted...")


ram = Employee(101, "Ram", "IT", 45000)
ram.showDetails()

del ram

shyam = Employee(102, "Shyam", "HR", 46000)
shyam.showDetails()

del shyam

mac = Employee(103, "Mac", "IT", 50000)
mac.showDetails()