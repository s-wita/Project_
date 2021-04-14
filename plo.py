import time

print("Hello in Hangman game")

time.sleep(1)

print("Starting guessing...")
time.sleep(0.5)

word = "secret"

guesses = ""

turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("-")
            failed += 1
    if failed == 0:
        print("You won !!!")
        break

    guess  = input("Give a word: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have " + str(turns) + " left")
        if turns == 0:
            print("You lose")