import random

# GLobal varibles
playerChips = 100
wager = 0


# Generates list of 5 numbers
def generate5Numbers():
    numbers = []
    numbers = random.sample(range(10), 5)
    return numbers


# Generates list of 7 numbers
def generate7Numbers():
    numbers = []
    numbers = random.sample(range(10), 7)
    return numbers


# Pick 1 numbr game
def pick1Number():
    lottery = generate5Numbers()
    global wager
    try:
        playerGuess = int(input("Pick a number between 0 and 9: "))

        if playerGuess in lottery:
            print("You guessed correctly! You win 1 times your wager!\n")
            return int(wager)
        else:
            print("You guessed incorrectly. You lose your wager.\n")
            return int(-wager)
    except ValueError:
        print("Please enter a valid number.\n")
        pick1Number()


# Pick 2 numbers game
def pick2Numbers():
    lottery = generate5Numbers()
    global wager
    try:
        playerGuess = []
        print("Pick 2 numbers between 0 and 9: ")
        while len(playerGuess) < 2:
            guess = int(input(str(len(playerGuess) + 1) + ": "))
            if guess not in playerGuess:
                playerGuess.append(guess)
            else:
                print("You already picked that number.\n")
        if playerGuess[0] in lottery and playerGuess[1] in lottery:
            print("You guessed correctly! You win 2 times your wager!\n")
            return wager * 2
        else:
            print("You guessed incorrectly. You lose your wager.\n")
            return -wager
    except ValueError:
        print("Please enter a valid number.\n")
        pick2Numbers()


# Pick 7 game, jackpot game
def luckySeven():
    lottery = generate7Numbers()
    global wager
    try:
        playerGuess = []
        print("Pick 7 numbers between 0 and 9: ")
        while len(playerGuess) < 7:
            guess = int(input(str(len(playerGuess) + 1) + ": "))
            if guess not in playerGuess:
                playerGuess.append(guess)
            else:
                print("You already picked that number.\n")
        correct = 0
        for i in range(7):
            if playerGuess[i] in lottery:
                correct += 1
        if correct == 7:
            print("You guessed all 7 numbers correctly! You win 10 times your wager!\n")
            return wager * 10
        elif correct == 6:
            print("You guessed 6 numbers correctly! You win 5 times your wager!\n")
            return wager * 5
        else:
            print("You guessed", correct, "numbers correctly. You lose your wager.\n")
            return -wager
    except ValueError:
        print("Please enter a valid number.\n")
        luckySeven()


# Will display current chips player has
def currentChips():
    print("You have", playerChips, "chips.\n")


# Will display the banner
def banner():
    print("Welcome to the lottery game! You have", playerChips, "chips.\n")


# Will handle the wager
def wagerHandler():
    global wager
    while True:
        try:
            wager = int(input("How much would you like to wager? (1-10) "))
            if 1 <= wager <= 10:
                break
            else:
                print("Wager must be between 1 & 10\n")
        except ValueError:
            print("Please enter a valid number.\n")
            wagerHandler()


# Will display the menu
def menu():
    print("1. Pick 1 number")
    print("2. Pick 2 numbers")
    print("3. Pick 7 numbers")
    print("4. Quit")


# Main function
def main():
    global playerChips
    global wager
    banner()
    while playerChips > 0:
        # Asks player for wager at start
        wagerHandler()
        # Ask player what game they want to play
        menu()
        try:
            choice = int(input("What would you like to do? "))
            if choice == 1:
                playerChips += pick1Number()
                currentChips()
            elif choice == 2:
                playerChips += pick2Numbers()
                currentChips()
            elif choice == 3:
                playerChips += luckySeven()
                currentChips()
            elif choice == 4:
                print("Thanks for playing!")
                break
            else:
                print("Please enter a valid number.\n")
        except ValueError:
            print("Please enter a valid number.\n")
    print("You have no more chips. Thanks for playing!\n")


main()
