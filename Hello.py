row = input("\nHi! What's your name?\n").capitalize()

def name_greetings():
    print("Hello, {}".format(row))
    return "The end of the questanary"

print(name_greetings())