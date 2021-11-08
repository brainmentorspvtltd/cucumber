x = 8
y = 12
z = x + y
z1 = x / y
z2 = x - y
z3 = x * y

print(z)
print("Sum is",z)
print("Sum of", x, "and", y, "is", z)

#int - %d
print("Sum is %d"%z)
print("Sum of %d and %d is %d"%(x,y,z))
print("Div of %d and %d is %f"%(x,y,z1))

print("Sum is {}".format(z))
print("Sum of {} and {} is {}".format(x,y,z))
print("Div of {} and {} is {:.2f}".format(x,y,z1))
print("Sum of {2} and {0} is {1}".format(y,z,x))

#f-strings - format strings
print(f"Sum of {x} and {y} is {z}")
print(f'Div of {x} and {y} is {z1:.2f}')

# multi-line print
print(f"""
     1. Add is {z}
     2. Sub is {z2}
     3. Div is {z1:.2f}
     4. Mul is {z3}
""")









