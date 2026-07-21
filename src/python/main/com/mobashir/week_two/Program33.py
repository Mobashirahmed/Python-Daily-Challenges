# Check whether at least one of two numbers is negative.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

at_leat_one_negative = (num1 < 0) or (num2 < 0)

print("Is at least one number is negative?", at_leat_one_negative)