# Global Variables
x = 12
y = 4

# Function Definition
def calc():
    # Local Variables
    x = 1
    x = x + 5

    global z
    z = x + 5
    print("Sum is",z)

# Function Calling
calc()
print(x,y,z)