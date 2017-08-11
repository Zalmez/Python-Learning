#!/user/bin/env python
"""Guessing.py, laget av cato myhre, 07.08.17
Dette programmet spør brukeren om å gjette et nummer mellom 1-100, hvis nummeret er rikig la
"""
import random
import logging
def randomInt(minVal, maxVal):
    #Checks if randomInt has it's required values or not, then returns a message if there is no values
    if minVal is None:
         logging.debug("minVal has not been assigned to a value")
    elif maxVal is None:
        logging.debug("maxVal has not been assigned to a value")
    else:
        randomVal = random.randint(minVal, maxVal)
    return randomVal

def main():
    print ("Guess a number between 1 and 100")
    #randomNumber = "35" #debugging verdi
    #randomNumber = str(random.randint(1,100))
    randomNumber = randomInt(1, 100)
    found = False


    while not found:
        userGuess = input("Your guess: ")
        userGuess = int(userGuess)
        if userGuess == randomNumber:
            print ("You got it right!")
            found = True
        elif userGuess > randomNumber:
            print ("Guess Lower!")
        else:
            print("Guess Higher")

if __name__ == '__main__':
    main()
    