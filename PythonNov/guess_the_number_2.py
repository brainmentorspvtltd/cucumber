# Guess the number game
import random

cpu = random.randint(1,100)
count = 5
while True:
    num = int(input("Guess the number : "))

    if cpu == num:
        print("Congrats you guessed the number....")
        break
    elif num > cpu:
        print("You have guessed a large number...")
    elif num < cpu:
        print("You have guessed a smaller number...")
    else:
        print("Invalid Input...")

    count -= 1
    print("Chances Left :",count)

    if count == 0:
        print("You Lose..Number was",cpu)
        break
    

    
