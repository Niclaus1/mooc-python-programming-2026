# Write your solution here
from random import choice

def roll(die : str):
    dieA = [3, 3, 3, 3, 3, 6]
    dieB = [2, 2, 2, 5, 5, 5]
    dieC = [1, 4, 4, 4, 4, 4]
    
    match die.upper().strip():
        case "A":
            return choice(dieA)
        case "B":
            return choice(dieB)
        case "C":
            return choice(dieC)
        case _:
            return
def play(die1 :str, die2:str, times:int):
    player1 = 0
    player2 = 0
    aTie = 0
    
    for i in range(times):
        if roll(die1) == roll(die2):
            aTie += 1
        elif roll(die1) > roll(die2):
            player1 += 1
        else:
            player2 += 1

    return (player1,player2,aTie)

if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)