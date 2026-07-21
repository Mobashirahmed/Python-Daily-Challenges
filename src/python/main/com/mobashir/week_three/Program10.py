# Take your height and weight as input and calculate BMI.
height = float(input("Enter height (in meters): "))
weight = float(input("Enter weight (in kg): "))

BMI = (weight / (height ** 2))
print("BMI is ", BMI)
