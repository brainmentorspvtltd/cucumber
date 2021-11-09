# Guess the number game
import random

cpu = random.randint(1,100)
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
