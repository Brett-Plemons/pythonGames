from random import randint
from os import system

i = 0
x = 0
print("Do you want 1 or 2 players?")
players = int(input())

while True:
    print("It's rock, paper, scissors time!")

    print("Player 1 make your move!")
    player = input().lower()

    if player == "rock":
        player = 1
    elif player == "paper":
        player = 2
    elif player == "scissors":
        player = 3
    else:
        print("rock, paper, scissors are your only options dum-dum!")

    system('cls')

    if players == 1:
        player2 = randint(1, 3)
        if player2 == 1:
            print("Computer played Rock!")
        elif player2 == 2:
            print("Computer played Paper!")
        else:
            print("Computer played Scissors!")

    else:
        print("Player 2 make your move!")
        player2 = input().lower()

        if player2 == "rock":
            player2 = 1
        elif player2 == "paper":
            player2 = 2
        elif player2 == "scissors":
            player2 = 3
        else:
            print("rock, paper, scissors are your only options dum-dum!")

    if player == player2:
        print("Its a tie!")
        print(f"{x} points for Player 1 to {i} points for Player 2")
    elif player2 != 3:
        if player > player2:
            i += 1
            print("1 point Player 1")
            print(f"{x} points for Player 1 to {i} points for Player 2")
        elif player < player2:
            i += 1
            print("1 point Player 2")
            print(f"{x} points for Player 1 to {i} points for Player 2")
    elif player2 == 3 and player == 1:
        x += 1
        print("1 Point Player 1")
        print(f"{x} points for Player 1 to {i} points for Player 2")
    else:
        i += 1
        print("1 Point Player 2")
        print(f"{x} points for Player 1 to {i} points for Player 2")

    if x == 2 or i == 2:
        print(f"Game over {x}-{i}")
        repeat = input("Would you like to play again? y/n ")
        if repeat[0] == "y":
            x = 0
            i = 0
        else:
            break
