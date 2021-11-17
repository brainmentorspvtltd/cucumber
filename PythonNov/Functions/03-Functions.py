# positional arguments

# Default arguments
def calc(x=0,y=0):
    z = x + y
    print("Sum is",z)

calc()
calc(5)
calc(5,6)
calc(7,y=6)
calc(x=6,y=7)

# calc()
# calc(5)
# calc(5,7)

# Keywords arguments
# calc(8,y=7)
# calc(x=7, y=10)
# calc(7,10)
# calc(y=10, x=7)
