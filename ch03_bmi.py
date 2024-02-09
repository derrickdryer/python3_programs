height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))
bmi = weight * 703/(height**2)
if bmi < 18.5:
    print("Body Mass Index:", format(bmi, '.2f'))
    print("Your BMI shows you are underweight.")
elif bmi >=18.5 and bmi < 25:
    print("Body Mass Index:", format(bmi, '.2f'))
    print("Your BMI is optimal.")
else:
    print("Body Mass Index:", format(bmi, '.2f'))
    print("Your BMI shows you are overweight. EAT A SALAD!!!")