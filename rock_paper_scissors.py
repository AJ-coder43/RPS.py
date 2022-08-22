from random import randint

#list of moves
t = ["Rock", "Paper", "Scissors"]

#computer assigned random move
computer = t[randint(0,2)]

#player = false
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print ("You win!", player, "smashes", computer)
    elif player== "Paper":
        if computer == "Scissors":
            print("You lose!!!", computer, "cut", player)
        else:
            print("You win!", player, "cut", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid move. Review your input.")
        
    #reset loop
    player = False
    computer = t[randint(0,2)]
        