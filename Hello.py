def name_greetings():
    row = input("\nHi! What's your name?\n").capitalize()
    print("Hello, {}".format(row))
    return "The end of the questanary"

print(name_greetings())