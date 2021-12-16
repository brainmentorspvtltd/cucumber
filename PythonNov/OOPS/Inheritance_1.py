from datetime import  datetime as dt

class Bank:
    def __init__(self, name, acc_type):
        self.name = name
        self.accType = acc_type
        self.date = dt.now().date()

    def show(self):
        print("Bank Details...")
        print("Account opened in", self.date)
        print("Name :", self.name)
        print("Account Type :", self.accType)

class Person():
    def __init__(self, name, occ, age, accType):
        self.name = name
        self.occupation = occ
        self.age = age
        self.bankAcc = Bank(name, accType)
        # bankAcc.show()

    # def show(self):
    #     print("Personal Details...")
    #     print(self.name, self.occupation, self.age)

class Employee(Person):
    def __init__(self, name, occ, age, accType, company, sal):
        super(Employee, self).__init__(name, occ, age, accType)
        self.company = company
        self.sal = sal

    def showEmp(self):
        print("Personal Details...")
        print(self.name, self.occupation, self.age)

        print("Employee Details : ")
        print("Company name :",self.company)
        print("Salary is :",self.sal)

        self.bankAcc.show()

obj = Employee("Ram","Emp",40,"Saving","TCS",45000)
obj.showEmp()

