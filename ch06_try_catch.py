def main():
    try:
        num = float(input("Enter a number: "))
        print("Your number is", num)

    except ValueError:
        print("That was not a valid number. Please enter a valid number.")
        main()


main()
