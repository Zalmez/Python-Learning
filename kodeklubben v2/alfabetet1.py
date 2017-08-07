#!/usr/bin/env python
#pylint: disable=C0103
def getAlphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
    return alphabet

def encode(letter, secret):
    pos = getAlphabet().find(letter)

    newpos = (pos-int(secret))

    if newpos >= 29:
        newpos = newpos - 29
    return getAlphabet()[newpos]

def decode(letter, secret):
    pos = getAlphabet().find(letter)
    newpos = (pos-int(secret))

    if newpos < 0:
        newpos = newpos + 29 
    return getAlphabet()[newpos]

def getCommand():
    command = input("Decode or encode?: ")
    return command

def main():
    command = getCommand()
    if command == "decode":
        secret = input("What's the secret number?: ")
        message = input("The message you want to decode: ")
        output = ""

        for character in message:
            if character in getAlphabet():
                output = output + decode(character, secret)
            else:
                output = output + character
    if command == "encode":
        secret = input("What's the secret number?: ")
        message = input("The message you want to encode: ")
        output = ""

        for character in message:
            if character in getAlphabet():
                output = output + encode(character, secret)
            else:
                output = output + character

    else:
        print("Could not find " + command + ". Try decode or encode")
        main()
    print(output)

main()
