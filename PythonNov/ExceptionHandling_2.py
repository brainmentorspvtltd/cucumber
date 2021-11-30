try:
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    z1 = x + y
    z2 = x + y
    z3 = x / y
    z4 = x * y
except (ValueError, ZeroDivisionError, FloatingPointError) as ex:
    # print("Invalid Input...")
    print(ex)
except BaseException as ex:
    print(ex)
else:
    print("Sum is", z1)
    print("Sub is", z2)
    print("Div is", z3)
    print("Mul is", z4)