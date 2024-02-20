def main():
    try:
        x = float(input("Enter a number: "))
        y = float(input("Enter another number: "))

        print("What would you like to do?")
        print("1) Add the numbers")
        print("2) Subtract the numbers")
        print("3) Multiply the numbers")
        print("4) Divide the numbers")
        userInput = input("Enter a selection: ")

        if userInput == 1:
            print(add(x, y))
        elif userInput == 2:
            print(subtract(x, y))
        elif userInput == 3:
            print(multiply(x, y))
        elif userInput == 4:
            print(divide(x, y))
        else:
            print("Invalid selection")
    except ValueError as e:
        print("Invalid input:", e)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


main()
