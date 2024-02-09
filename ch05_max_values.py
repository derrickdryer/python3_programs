num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def max_value(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print("The maximum value is", max_value(num1, num2))
