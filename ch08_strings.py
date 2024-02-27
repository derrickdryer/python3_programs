userDate = input("Enter a date (mm/dd/yyyy): ")

monthName = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def extractDate(userDate):
    month = userDate[0:2]
    day = userDate[3:5]
    year = userDate[6:10]
    if userDate[2] == "/":
        day = userDate[3]
        year = userDate[5:10]
    return month, day, year


def main():
    month, day, year = extractDate(userDate)
    month = int(month)
    month -= 1
    day = int(day)
    year = int(year)
    print("The date is", monthName[month], str(day) + ",", year)


main()
