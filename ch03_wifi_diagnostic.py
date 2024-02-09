print("===== Wi-Fi Diagnostic Tree =====")
print("Reboot the computer and try to connect.")
answer = input("Did this fix the problem? (yes or no) ")
if answer == "no":
    print("Reboot that router and try to connect.")
    answer = input("Did this fix the problem? (yes or no) ")
    if answer == "no":
        print("Make sure the cables between the router and modem are plugged in firmly.")
        answer = input("Did this fix the problem? (yes or no) ")
        if answer == "no":
            print("Move the router to a new location.")
            answer = input("Did this fix the problem? (yes or no) ")
            if answer == "no":
                print("Get a new router")
            else:
                print("Router is fixed. Program Ending.")
        else:
            print("Router is fixed. Program Ending.")
    else:
        print("Router is fixed. Program Ending.")
else:
    print("Router is fixed. Program Ending.")