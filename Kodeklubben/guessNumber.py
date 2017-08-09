from random import randint

correct_number = randint(1, 100)


def guessingGame():
    print("Guess a number between 1-100")
    guessed_number = 0
    for i in range(12):
        usr_input = input("Please guess a number: ")
        guessed_number = usr_input
        if guessed_number != correct_number:
            i = i+1
            if(guessed_number > correct_number):
                print("lower!")
            elif guessed_number < correct_number:
                print("Higher")
        elif guessed_number == correct_number:
            print("You guessed correctly!")
            i = 12

guessingGame()
    