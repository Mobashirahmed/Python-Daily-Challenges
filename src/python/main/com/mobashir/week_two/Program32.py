# Check whether both entered numbers are positive.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

both_positive = (num1 > 0) and (num2 > 0)

print("Are both numbers positive?", both_positive)
