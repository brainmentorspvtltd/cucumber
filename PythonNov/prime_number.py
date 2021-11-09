# Prime Number
num = 17
prime = False
for i in range(2, num//2):
    if num % i == 0:
        prime = False
        break
    else:
        prime = True

if prime:
    print("Prime Number...")
else:
    print("Not Prime...")
