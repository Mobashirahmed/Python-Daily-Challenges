# Simple Electricity Bill Calculator

# Get the number of units consumed from the user
units_consumed = float(input("Enter the total units consumed: "))

# Get the cost per individual unit from the user
cost_per_unit = float(input("Enter the cost per unit: "))

# Calculate the total bill amount
total_bill = units_consumed * cost_per_unit

# Display the final calculated bill amount
print(f"Total Electricity Bill: {total_bill:.2f}")