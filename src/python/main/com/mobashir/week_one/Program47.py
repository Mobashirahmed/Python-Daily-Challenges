# Salary Calculator Program

# Step 1: Get user inputs for basic pay and allowance percentages
basic_salary = float(input("Enter the Basic Salary: "))
hra_percentage = float(input("Enter the HRA percentage: "))
da_percentage = float(input("Enter the DA percentage: "))

# Step 2: Calculate HRA and DA amounts based on the Basic Salary
hra_amount = (basic_salary * hra_percentage) / 100
da_amount = (basic_salary * da_percentage) / 100

# Step 3: Compute the Gross Salary
gross_salary = basic_salary + hra_amount + da_amount

# Step 4: Display the itemized earnings breakdown
print("\n--- Salary Slip Summary ---")
print(f"Basic Salary: {basic_salary:.2f}")
print(f"HRA Amount:   {hra_amount:.2f}")
print(f"DA Amount:    {da_amount:.2f}")
print(f"---------------------------")
print(f"Gross Salary: {gross_salary:.2f}")