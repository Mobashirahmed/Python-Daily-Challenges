principal = float(input("Enter your Principal amount: $"))
rate = float(input("Enter the Rate: "))
time = int(input("Enter the time(in years): "))

interest = (principal * rate * time) / 100

print(f"The interest is: ${interest:.2f}")