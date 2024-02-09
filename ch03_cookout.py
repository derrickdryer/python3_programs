## Base variables
hotdogPackage = 10
hotdogBuns = 8

## Gather user input
attendees = int(input("How many people are attending the cookout? "))
dogPerPerson = int(input("How many hotdogs will each person get? "))

## Calculate user input to figure out required hotdogs
reqHotdogs = attendees * dogPerPerson

## Calculate minimum amount of hotdog packages needed
minHotdogPck = round(reqHotdogs / hotdogPackage)
## Calculate minimum amount of hotdog bun packages needed
minHotdogBun = round(reqHotdogs / hotdogBuns)

## Print required info
print("Minimum packages of hotdogs: ", minHotdogPck)
print("Minimum packages of buns: ", minHotdogBun)
## Calculate Left Over Hotdogs if true
if (minHotdogPck * hotdogPackage) > reqHotdogs:
    leftoverHotdogs = (minHotdogPck * hotdogPackage) - reqHotdogs
    leftoverBuns = (minHotdogBun * hotdogBuns) - reqHotdogs
    ## Print if true
    print("Leftover hotdogs: ", leftoverHotdogs)
    print("Leftover hotdog buns: ", leftoverBuns)