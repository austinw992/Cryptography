alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "XPMGTDHLYONZBWEARKJUFSCIQV"


# Defined Main for when user inputs their option and then inputs their phrase
# while statement under these conditions only
def main():
    keepGoing = True
    while keepGoing:
        response = menu()
        if response == "1":
            plain = input("text to be encoded: ")
            print(encode(plain))
        elif response == "2":
            coded = input("code to be decyphered: ")
            print(decode(coded))
        elif response == "0":
            print("Thanks for doing secret spy stuff with me.")
            keepGoing = False
        else:
            print("I don't know what you want to do...")


# provides user options of what they would want to do
def menu():
    print("Here's your menu options")
    print("(0) Quit \n (1) Encode \n (2) Decode \n")
    word = input("What would you like to perform? ")
    return word


# user chooses to encode then scramble from alpha to key
def encode(plain):
    phrase = plain.upper()
    phrase = phrase.replace(" ","")
    #storage for the letters being replaced
    phrasetwo = " "
    i = 0

#depending on the length of the word given, the loop will continue until i reaches zero
    while i < len(phrase):
        alpha_place = alpha.find(phrase[i])
        key_place = key[alpha_place]
        #cacatination to avoid the letters go into vertical
        phrasetwo += key_place
        #we need to keep the user's input as a string not a float or integer
        str(alpha_place)
        i = i + 1
    return phrasetwo


# user choose to decode scramble the phrase from key to alpha
def decode(coded):
    mystery = coded.upper()
    mystery = mystery.replace(" ","")
    #storage for the letters being replaced
    mysterytwo = " "
    i = 0

#depending on the length of the word given, the loop will continue until i reaches zero, replacing each letter
    while i < len(mystery):
        key_place = key.find(mystery[i])
        alpha_place = alpha[key_place]
        #cacatination to avoid the letters go into vertical
        mysterytwo += alpha_place
        #we need to keep the user's input as a string not a float or integer
        str(key_place)
        i = i + 1
    return mysterytwo



main()
#menu()
#encode()
#decode()