def main():
    try:
        num = float(input("Enter a number: "))
        num2 = float(input("Enter a number to divide by: "))

        num3 = num / num2

        print("The result of dividing", num, "by", num2, "is", num3)

    except ZeroDivisionError:
        print("You can't divide by zero. Please enter a valid number.")
        main()

    except ValueError:
        print("That was not a valid number. Please enter a valid number.")
        main()


main()
