# import covid_api

def atm():
    total = 10000
    pin = input("Enter your PIN : ")
    assert (pin == "1234"), "Invalid PIN..."
    print("Welcome User...")

    amount = int(input("Enter the amount : "))
    assert total > amount, "Insufficient Balance..."
    total -= amount
    print("Remaining balance is",total)

try:
    atm()
except AssertionError as err:
    print(err)
    atm()