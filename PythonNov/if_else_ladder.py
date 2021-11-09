#If Else Ladder
x,y,z = 10,21,34

#Logical Operators - and (&&), or (||), not (!)
if x > y and x > z:
    print("X is greatest")
elif y > x and y > z:
    print("Y is greatest")
else:
    print("Z is greatest")

res = "X" if x > y and x > z else "Y" if y > x and y > z else "Z"
print(res,"is greatest...")
