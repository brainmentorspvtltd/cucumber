# Connect Model and View
import Model

def register(name, pwd, dept, salary):
    Model.registerEmp(name, pwd, dept, salary)

def login(name, pwd):
    msg = Model.loginEmp(name, pwd)
    return msg
