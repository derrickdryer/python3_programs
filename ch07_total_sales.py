weeklySales = [
    ["Monday", 0],
    ["Tuesday", 0],
    ["Wednesday", 0],
    ["Thursday", 0],
    ["Friday", 0],
    ["Saturday", 0],
    ["Sunday", 0],
]
totalSales = 0.0


def getSales():
    global weeklySales
    global totalSales
    try:
        for day in weeklySales:
            sales = float(input("Enter the sales for " + day[0] + ": "))
            day[1] = sales
            totalSales += sales
    except ValueError:
        print("You must enter a valid number.")
        getSales()


def highestDay():
    global weeklySales
    highestDay = max(weeklySales)
    print(
        "The highest sales day was"
        + str(highestDay[0])
        + " with $"
        + str(highestDay[1])
        + ". \n"
    )


def lowestDay():
    global weeklySales
    lowestDay = min(weeklySales)
    print(
        "The lowest sales day was"
        + str(lowestDay[0])
        + " with $"
        + str(lowestDay[1])
        + ". \n"
    )


def printSales():
    global weeklySales
    for day in weeklySales:
        print(day[0] + ": $" + str(day[1]))


def main():
    getSales()
    printSales()
    highestDay()
    lowestDay()
    print("The total sales for the week was $" + str(totalSales))


main()
