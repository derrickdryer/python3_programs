import random

number = random.randint(1, 100)

def user_guess():
    guess= int(input("Enter a number between 1 and 100: "))
    return guess

def compare(number, guess, repeat):
    if number == guess:
        return "Congratulations! You guessed the correct number."
    elif number < guess:
        return "You guessed too high. Try again."
    else:
        return "You guessed too low. try again."

def main():
    repeat = True
    while repeat:
        guess = user_guess()
        result = compare(number, guess, repeat)
        print(result)
        if number == guess:
            repeat = False

main()