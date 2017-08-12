alphabet = u"abcdefghijklmnopqrstuvwxyzæøå"

def encode(letter, secret):
    pos = alphabet.find(letter)

    newpos = (pos-secret)

    if newpos >= 29:
        newpos = newpos - 29
    return alphabet[newpos]

def decode(letter, secret):
    pos = alphabet.find(letter)
    newpos = (pos-int(secret))

    if newpos < 0:
        newpost=(pos-secret)
    return alphabet[newpos]

def main():
    command = input("Decode or encode?: ")
    secret = input("What's the secret number?: ")
    if(command=="decode"):
        message = input("The message you want to decode: ")
        output = ""

        for character in message:
            if character in alphabet:
                output = output + decode(character, secret)
            else:
                output = output + character
    if(command=="encode"):
        message = input("The message you want to encode: ")
        output = ""

        for character in message:
            if character in alphabet:
                output = output + encode(character, secret)
            else:
                output = output + character


    print(output)

main()
