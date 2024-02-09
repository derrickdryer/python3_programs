import random

def player_choice():
    number = int(input("Pick a number: 1. Rock | 2. Paper | 3. Scissors \n"))
    if number < 1 and number > 3:
        print("That is not a valid option. Pick again.")
        player_choice()
    else:
        return number

def main():
    cpu_choice = random.randint(1, 3)
    if player_choice() == cpu_choice:
        print("Its a tie. Try again!")
        player_choice()
        main()
    elif player_choice() == 1:
        if cpu_choice == 2:
            print("CPU Wins: Paper beats Rock!")
        elif cpu_choice == 3:
            print("Player Wins: Rock beats Scissors!")
    elif player_choice() == 2:
        if cpu_choice == 1:
            print("Player Wins: Paper beats Rock!")
        elif cpu_choice == 3:
            print("CPU Wins: Scissors beats Paper!")
    elif player_choice() == 3:
        if cpu_choice == 1:
            print("CPU Wins: Rock beats Scissors!")
        elif cpu_choice == 2:
            print("Player Wins: Scissors beats Paper!")

main()