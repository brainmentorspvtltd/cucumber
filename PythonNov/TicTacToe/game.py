import random

numbers = [i for i in range(0,9)]
occupied = []

winning_combinations = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def checkWinner(pos, ch):
    for i in range(len(winning_combinations)):
        if pos in winning_combinations[i]:
            index = winning_combinations[i].index(pos)
            winning_combinations[i][index] = ch
    for i in range(len(winning_combinations)):
        if winning_combinations[i][0] == ch and winning_combinations[i][1] == ch and winning_combinations[i][2] == ch:
            winner = pos
            return winner

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

def userMove(ch):
    pos = int(input("Enter your position : "))
    numbers[pos] = ch
    occupied.append(pos)
    gameBoard()

def cpuMove(ch):
    cpu_pos = random.randint(0,8)
    if cpu_pos not in occupied:
        print("CPU Moved on :",cpu_pos)
        numbers[cpu_pos] = ch
        occupied.append(cpu_pos)
        gameBoard()
    else:
        print(f"{cpu_pos} Position Already Occupied...")
        cpuMove(ch)

def game():
    gameBoard()

    ch = input("Enter your choice [0 / X] : ")
    if ch == "0":
        cpu = "X"
    else:
        cpu = "0"
    gameStatus = True
    while gameStatus:
        userMove(ch)
        cpuMove(cpu)

game()