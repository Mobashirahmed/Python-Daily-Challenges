# Extended Salary Calculator Program

# Step 1: Get user inputs for earnings and deductions
basic_salary = float(input("Enter the Basic Salary: "))
hra_percentage = float(input("Enter the HRA percentage: "))
da_percentage = float(input("Enter the DA percentage: "))

pf_percentage = float(input("Enter the PF deduction percentage: "))
professional_tax = float(input("Enter the flat Professional Tax deduction: "))

# Step 2: Compute allowance amounts
hra_amount = (basic_salary * hra_percentage) / 100
da_amount = (basic_salary * da_percentage) / 100

# Step 3: Compute total Gross Salary
gross_salary = basic_salary + hra_amount + da_amount

# Step 4: Compute deduction amounts (PF is calculated on Basic Salary)
pf_amount = (basic_salary * pf_percentage) / 100
total_deductions = pf_amount + professional_tax

# Step 5: Compute Net Salary
net_salary = gross_salary - total_deductions

# Step 6: Display the comprehensive salary slip
print("\n--- Complete Salary Slip ---")
print(f"Basic Salary:      {basic_salary:.2f}")
print(f"HRA Allowance:    +{hra_amount:.2f}")
print(f"DA Allowance:     +{da_amount:.2f}")
print(f"GROSS SALARY:      {gross_salary:.2f}")
print(f"----------------------------")
print(f"PF Deduction:     -{pf_amount:.2f}")
print(f"Professional Tax: -{professional_tax:.2f}")
print(f"TOTAL DEDUCTIONS:  {total_deductions:.2f}")
print(f"----------------------------")
print(f"NET SALARY:        {net_salary:.2f}")