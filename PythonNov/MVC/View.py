# UI - Input and Output
import Controller

def register():
    name = input("Enter Emp Name : ")
    dept = input("Enter Emp Dept : ")
    salary = int(input("Enter Emp Salary : "))
    Controller.register(name, dept, salary)

def login():
    pass

def main():
    while True:
        print("""
        1. Register Employee
        2. Login Employee
        3. Delete Employee
        4. Update Employee
        5. Search Employee
        """)

        ch = input("Enter your choice : ")
        operations = {
            "1" : register,
            "2" : login
        }
        operations.get(ch)()

main()