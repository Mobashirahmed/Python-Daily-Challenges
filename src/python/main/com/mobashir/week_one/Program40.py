days = int(input("Enter the number of days: "))

years = days // 365
months = (days % 365) // 30
days = (days % 365) % 30

print(f"The number of Years: {years}, Months: {months}, Days: {days}")