import random
import time 

ladder = {8: 26, 11:45, 15:22, 19: 38, 21: 79, 25:64, 28: 49, 50: 91, 61: 99, 66: 87, 77: 96} 
snake = {68: 2, 48: 9, 52: 11, 98: 13, 57: 17, 64: 24, 88: 52, 95: 77 , 25: 9 , 34: 12 ,43:12} 

Position1 = 0
Position2 = 0 

def move(Position):
    dice = random.randint(1,6)
    print(f"Dice:{dice}")
    Position = Position + dice
    
    if Position in snake :
        print("\nOhh My God !!! \nYou Got Bitten By Snake")
        Position = snake[Position]
        print(f"Current Position is :{Position}\n")
        time.sleep(1)
        
    elif Position in ladder:
        print("\nOhh Nice Played !!\nYou Got ladder to climb Up")
        Position = ladder[Position]
        print(f"Current Position is : {Position}\n")
        time.sleep(1)
        
    else:
        print(f"Current Position is: {Position}")
        print("\n")
        time.sleep(1)

    return Position


print("-Welcome To The Snake And Ladder Game-")
print("\n")

player1=input("Enter First Players Name : ")
player2=input("Enter Second Players Name : ")
time.sleep(1)

while True:
    A = input (f"\n{player1} Press Enter to throw Dice")
    Position1 = move(Position1)
    if Position1>=100:
        print(f"Game Over!!\n Congrats {player1} !! \n You Won The Game!!")
        break
    
    B = input (f"{player2} Press Enter to throw Dice")
    Position2 = move(Position2)
    if Position2>=100:
        print(f"Game Over!!\n Congrats {player2} !! \n You Won The Game!!")
        break
