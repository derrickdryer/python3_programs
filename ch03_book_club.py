books = int(input("Enter how many books you purchased this month: "))
if books >= 8:
    points = 60
    print("Points earned this month:", points)
elif books < 8 and books >= 6:
    points = 30
    print("Points earned this month:", points)
elif books < 6 and books >= 4:
    points = 15
    print("Points earned this month:", points)
elif books < 4 and books >= 2:
    points = 5
    print("Points earned this month:", points)
else:
    print("You did not purchase enough books to earn points this month.")