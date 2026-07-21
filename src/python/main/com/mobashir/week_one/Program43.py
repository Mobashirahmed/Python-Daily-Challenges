mark1 = int(input("Enter your Maths marks: "))
mark2 = int(input("Enter your Science marks: "))
mark3 = int(input("Enter your SSt marks: "))
mark4 = int(input("Enter your G.K marks: "))
mark5 = int(input("Enter your Computer marks: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

print(f"Your Percentage is: {percentage:.2f}%")