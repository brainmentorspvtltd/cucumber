import random

numbers = [i for i in range(1,10)]
gameset = {1,2,3,4,5,6,7,8,9}
def gameBoard():
    print("""
    {} | {} | {}
    ----------
    {} | {} | {}
    ----------
    {} | {} | {}
    """.format(numbers[0], numbers[1], numbers[2],
               numbers[3], numbers[4], numbers[5],
               numbers[6], numbers[7], numbers[8]))

def userinput():
    pos = int(input("Enter your Position [1..9] : "))
    if pos in gameset :
        gameset.remove(pos)
        return pos
    else:
        print("Invalid Position")
        userinput()

def cpuinput():
    pos = random.randint(1,9)
    if pos in gameset :
        gameset.remove(pos)
        return pos
    else:
        cpuinput()

def userMove(ch):
    pos = int(userinput())
    numbers[pos-1] = ch
    gameBoard()

def cpuMove(ch):
    pos = int(cpuinput())
    numbers[pos - 1] = ch
    gameBoard()

def game():
    gameBoard()
    ch = input("Enter your choice [0 / X] : ")
    if ch == "0":
        cpu = "X"
    else:
        cpu = "0"

    gameover = "False"
    turnof = "U"
    while(gameover == "False"):
        if turnof == "U":
            userMove(ch)
            turnof='C'
        else:
            cpuMove(cpu)
            turnof = 'U'
        if len(gameset) == 0 :gameover = "True"


game()


