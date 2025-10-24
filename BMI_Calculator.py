
while True:
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))
        BMI = weight/(height ** 2)
        if BMI <18.6:
            category = "underweight"
        elif 18.5 <= BMI <= 24.9:
            category = "normal"
        elif 25.0 <= BMI <= 29.9:
            category = "overweight"
        else:
            category = "obese"

        print(f"Your BMI is {BMI:.2f} and you are {category}")
        break
    except ValueError:
        print("Invalid input. Please enter the accurate number.")





