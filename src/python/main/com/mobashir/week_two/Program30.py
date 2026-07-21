# Check whether a number is greater than 10 and less than 100.

number = int(input("Enter a number: "))

is_in_range = (number > 10) and (number < 100)

print(f"Is {number} between 10 and 100?", is_in_range)