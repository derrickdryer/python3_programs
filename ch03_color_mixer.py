print("Choose from these colors: 1. red, 2. blue, 3. yellow")
color1 = input("Enter the first color: ")
if color1 == "1":
    print("You chose red")
    print("Choose from these colors: 1. blue, 2. yellow")
    color2 = input("Enter the second color: ")
    if color2 == "1":
        print("You chose blue")
        print("The result is purple")
    elif color2 == "2":
        print("You chose yellow")
        print("The result is orange")
    else:
        print("Invalid color choice")
elif color1 == "2":
    print("You chose blue")
    print("Choose from these colors: 1. red, 2. yellow")
    color2 = input("Enter the second color: ")
    if color2 == "1":
        print("You chose red")
        print("The result is purple")
    elif color2 == "2":
        print("You chose yellow")
        print("The result is green")
    else:
        print("Invalid color choice")
elif color1 == "3":
    print("You chose yellow")
    print("Choose from these colors: 1. red, 2. blue")
    color2 = input("Enter the second color: ")
    if color2 == "1":
        print("You chose red")
        print("The result is orange")
    elif color2 == "2":
        print("You chose blue")
        print("The result is green")
    else:
        print("Invalid color choice")
else:
    print("Invalid color choice")