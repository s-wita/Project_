from random import randint
items =["Paper","Rock","Scissors"]

comp = items[randint(0,2)]

player = False

while player == False:

    player = input("Paper,Rock,Scissors ? \nPlayer: ")

    if player == comp:
        print("Computer: ", comp)
        print("Tie!!!")
    elif player == "Paper":
        if comp == "Rock":
            print("Computer: ", comp)
            print("You win!!!")

        else:
            print("Computer: ", comp)
            print("You lose!!!")

    elif player == "Scissors":
        if comp == "Rock":
            print("Computer: ", comp)
            print("You lose!!!")
            continue

        else:
            print("Computer: ", comp)
            print("You win!!!")
    elif player == "Rock":
        if comp == "Scissors":
            print("Computer: ", comp)
            print("You win!!!")
            break
        else:
            print("Computer: ", comp)
            print("You lose!!!")
    continue

player = False
comp = items[randint(0,2)]
