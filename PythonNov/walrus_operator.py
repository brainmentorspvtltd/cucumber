#Walrus Operator
'''
x = 7
y = 12
z = x + y
print("Sum is",z)
'''
x, y = 7, 12
#print("Sum is",z := x + y)

#print(f"Sum of {x} and {y} is {(z := x + y)}")

print(f"""
     1. Add is {(z := x + y)}
     2. Sub is {(z1 := x - y)}
     3. Div is {(z2 := x / y)}
     4. Mul is {(z3 := x * y)}
""")




