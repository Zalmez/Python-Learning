#!/user/bin/env python
"""Guessing.py, laget av cato myhre, 07.08.17
Dette programmet spør brukeren om å gjette et nummer mellom 1-100, hvis nummeret er rikig la
"""
import random


def main():
    print ("Guess a number between 1 and 100")
    #randomNumber = "35" #debugging verdi
    randomNumber = str(random.randint(1,100))
    found = False


    while not found:
        userGuess = input("Your guess: ")

        if userGuess == randomNumber:
            print ("You got it right!")
            found = True
        elif userGuess > randomNumber:
            print ("Guess Lower!")
        else:
            print("Guess Higher")

if __name__ == '__main__':
    main()
    