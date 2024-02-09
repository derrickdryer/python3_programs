number = int(input("Enter a number between 0 and 36: "))
if number == 0:
    print("The color is green.")
elif number >= 1 and number <= 10:
    if number % 2 == 0:
        print("The color is black.")
    else:
        print("The color is red.")
elif number >= 11 and number <= 18:
    if number % 2 == 0:
        print("The color is red.")
    else:
        print("The color is black.")
elif number >= 19 and number <= 28:
    if number % 2 == 0:
        print("The color is black.")
    else:
        print("The color is red.")
elif number >= 29 and number <= 36:
    if number % 2 == 0:
        print("The color is red.")
    else:
        print("The color is black.")
else:
    print("Error: The number must be between 0 and 36.")