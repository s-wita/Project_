import random

number = random.randint(1,10)
hide_number = 0
print("chose number from 1 to 10")
while hide_number < 5:
    guess = int(input())
    hide_number += 1
    if number < guess:
        print("The number is lower")
    elif number > guess:
        print("The number is higher")
    elif number == guess:
        print("YOU WIN !!!")
    else:
        print("The number was " + str(number))

