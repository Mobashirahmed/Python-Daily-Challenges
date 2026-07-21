num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print("First number: ", num1)
print("Second number: ", num2)
print("Third number: ", num3)

# Finding max of first two
max_of_two = (num1 + num2 + abs(num1 - num2))/2

# Comparing the max_of_two with last one
largest = (num3 + max_of_two + abs(num3 - max_of_two))/2

print("Largest number: ", largest)