def atm():
    total = 10000
    pin = input("Enter your PIN : ")
    if pin == "1234":
        print("Welcome User...")
    else:
        raise ValueError("Invalid PIN...")

    amount = int(input("Enter the amount : "))
    if total < amount:
        raise ValueError("Insufficient Balance...")
    else:
        total -= amount
    print("Remaining balance is",total)

try:
    atm()
except ValueError as err:
    print(err)
    atm()