# Imports
import random
import time
# Game was running too fast, added time.sleep() to slow it down to make it readable
# Reference: https://www.digitalocean.com/community/tutorials/python-time-sleep

# Global Variables
player_score = 0
cpu_score = 0
current_yard = 20
yards_to_score = 80
first_down = 10
yards_to_first_down = 10
plays_to_first_down = 4
yards_gained_in_turn = 0
current_turn = 1

# General game difficulty
difficulty_conservative = 15
difficulty_risky = 65

# Welcome Message, displays once on start
print('''
    WELCOME TO THE FOOTBALL GAME!
    ============================
    You will be playing against the CPU.
    You and the CPU each get two turns.
    The player can use run, pass and kick plays.
    Each play besides kick has risky and conservative types.
    Kick plays can only be done within 50 yards.
    The farther from the endzone the harder a kick is.
    
    Touchdowns = 7 Points
    Fieldgoals = 3 Points
    
    GOOD LUCK!!!\n''')
continue_game = input("\nPress enter to start.\n")

# Main Menu
def play_menu():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Choose your play:")
    print("1. Run")
    print("2. Pass")
    if current_yard > 50:
        print("3. Kick")
    print("4. Quit")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    play_choice = int(input("Enter your choice: "))
    return play_choice

# Run Play
def run_play():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Choose your run play:")
    print("1. Conservative")
    print("2. Risky")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    run_choice = int(input("Enter your choice: "))
    return run_choice

# Calculate Run Play Result
def run_play_result(run_choice):
    global difficulty_conservative
    global difficulty_risky
    if run_choice == 1:
        run_success = random.randint(1, 100)
        if run_success >= difficulty_conservative:
            run_result = random.randint(1, 5)
        else:
            run_result = 0
    elif run_choice == 2:
        run_success = random.randint(1, 100)
        if run_success >= difficulty_risky:
            run_result = random.randint(5, 15)
        else:
            run_result = random.randint(-2, 0)
    else: 
        print("Invalid choice.")
        return run_play()
    return run_result

# Pass Play
def pass_play():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Choose your pass play:")
    print("1. Short")
    print("2. Long")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    pass_choice = int(input("Enter your choice: "))
    return pass_choice

# Calculate Pass Play Result
def pass_play_result(pass_choice):
    global difficulty_conservative
    global difficulty_risky
    if pass_choice == 1:
        pass_success = random.randint(1, 100)
        if pass_success >= difficulty_conservative:
            pass_result = random.randint(3, 10)
        else:
            pass_result = 0
    elif pass_choice == 2:
        pass_success = random.randint(1, 100)
        if pass_success >= difficulty_risky:
            pass_result = random.randint(10, 50)
        else:
            pass_result = random.randint(-8, 0)
    else:
        print("Invalid choice.")
        return pass_play()
    return pass_result

# Kick Play, Closer is easier, Farther is harder
def kick_play(current_yard):
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("> You are attempting a field goal.")
    print("> The closer you are, the easier it is.")
    print("> The farther you are, the harder it is.")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    wait = input("Press enter to continue.")
    if current_yard == 50:
        kick_chance = random.randint(1, 25)
    elif current_yard > 50 and current_yard <= 60:
        kick_chance = random.randint(1, 50)
    elif current_yard > 60 and current_yard <= 70:
        kick_chance = random.randint(1, 75)
    else:
        kick_chance = random.randint(1, 100)
    return kick_chance

# Calculate Kick Play Result
def kick_play_result(kick_chance, current_yard):
    if kick_chance > (current_yard * 2):
        print("\n>>> The field goal is good!")
        kick_result = 3
    else:
        print("\n>>> The field goal is no good.")
        kick_result = 0
    return kick_result

# CPU Play is randomly determined to be 0, 3, or 7
def computer_play():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("> The computer is now on offense. Let's see what happens.")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    wait = input("Press enter to continue.")
    computer_score = random.choice([0, 3, 7])
    time.sleep(0.4)
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    if computer_score == 0:
        print(">>> The computer's possession resulted in no points.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif computer_score == 3:
        print(">>> The computer's possession resulted in a field goal.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif computer_score == 7:
        print(">>> The computer's possession resulted in a touchdown.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    return computer_score

# Define Player Turn
def player_turn():
    global player_score
    global current_yard
    global current_turn
    global yards_gained_in_turn
    global yards_to_first_down
    yards_gained_in_turn = 0
    yards_to_first_down = 10
    attempts = 0
    while yards_gained_in_turn < 10 and attempts < 4:
        play_choice = play_menu()
        if play_choice == 1:
            run_choice = run_play()
            run_result = run_play_result(run_choice)
            current_yard += run_result
            yards_gained_in_turn += run_result
            yards_to_first_down -= run_result
            yard_result(run_result)
            attempts += 1
            if current_yard < 0:
                print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print(">>> You are at your own end zone. Turnover on downs.")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            if check_for_touchdown():
                break
        elif play_choice == 2:
            pass_choice = pass_play()
            pass_result = pass_play_result(pass_choice)
            current_yard += pass_result
            yards_gained_in_turn += pass_result
            yards_to_first_down -= pass_result
            yard_result(pass_result)
            attempts += 1
            if current_yard < 0:
                print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print(">>> You are at your own end zone. Turnover on downs.")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            if check_for_touchdown():
                break
        elif play_choice == 3:
            kick_chance = kick_play(current_yard)
            kick_result = kick_play_result(kick_chance, current_yard)
            player_score += kick_result
            break
        elif play_choice == 4:
            print("You chose to quit the game.")
            exit()
        else:
            print("Invalid choice.")
        time.sleep(0.4)
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"> Current yards: {current_yard}")
        print(f"> Yards to first down: {max(0, yards_to_first_down)}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        if attempts == 4 and yards_gained_in_turn < 10:
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(">>> Turnover on downs. It's the computer's turn.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        elif yards_gained_in_turn >= 10 and check_for_touchdown() == False and current_yard < 100:
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(">>> First down! It's still your turn.")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            player_turn()

# Display current yard line
def current_yard_display(current_yard):
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("> The current yard line is: ", current_yard)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

#Display Score Board
def score_board(player_score, cpu_score):
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("> The current score is:")
    print("> Player: ", player_score)
    print("> Computer: ", cpu_score)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Display Yard Result
def yard_result(yard_result):
    time.sleep(0.4)
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    if yard_result < 0:
        print(">> You lost ", abs(yard_result), " yards. < - >")
    elif yard_result == 0:
        print(">> You gained no yards.")
    else:
        print(">> You gained ", yard_result, " yards. < + >")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Display Final Score & Win/Loss/Tie
def final_score(player_score, cpu_score):
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("> The final score is:")
    print("> Player: ", player_score)
    print("> Computer: ", cpu_score)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    if player_score > cpu_score:
        print("\n>>> You win! :)")
    elif player_score < cpu_score:
        print("\n>>> You lose. :()")
    else:
        print("\n>>> It's a tie. :|")

# Check for touchdown
def check_for_touchdown():
    global player_score
    global current_yard
    if current_yard >= 100:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Touchdown! You scored 7 points.")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        player_score += 7
        current_yard = 20
        return True
    return False

# Main Game Loop
def main():
    global player_score
    global cpu_score
    global current_yard
    global current_turn
    while current_turn <= 2:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"> Turn {current_turn}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        time.sleep(0.4)
        current_yard_display(current_yard)
        time.sleep(0.4)
        player_turn()
        time.sleep(0.4)
        score_board(player_score, cpu_score)
        time.sleep(0.4)
        computer_score = computer_play()
        cpu_score += computer_score
        current_turn += 1
    final_score(player_score, cpu_score)

main()