# This program will tell the user an interpretation of their BMI value

weight = float(input("Enter your weight in kg: "))  #My Weight Example: 64kg
height = float(input("Enter your height in m: "))   #My Height Example: 1.71

bmi = weight / height**2   #Formula

if bmi < 18.5:
    print(f"\nYour bmi is {bmi}, you are underweight")
elif bmi > 18.5 and bmi <= 25:
    print(f"\nYour bmi is {bmi}, you are normal weight")
elif bmi > 25 and bmi <= 30:
    print(f"\nYour bmi is {bmi}, you are overweight")
elif bmi > 30 and bmi <= 35:
    print(f"\nYour bmi is {bmi}, you are obese")
elif bmi > 35:
    print(f"\nYour bmi is {bmi}, you are clinically obese")
