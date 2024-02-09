userAge = int(input("Enter your age: "))

if userAge <= 1:
    print("You are an infant.")
elif userAge > 1 and userAge < 13:
    print("You are a child.")
elif userAge > 13 and userAge < 20:
    print("You are a teenager.")
elif userAge > 20:
    print("You are an adult.")