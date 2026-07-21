# Extended Electricity Bill Calculator

# Step 1: Get inputs from the user
units_consumed = float(input("Enter the total units consumed: "))
cost_per_unit = float(input("Enter the cost per unit: "))
fixed_charge = float(input("Enter the fixed monthly charge: "))
gst_percentage = float(input("Enter the GST rate (in %): "))

# Step 2: Calculate the energy charge based on consumption
energy_charge = units_consumed * cost_per_unit

# Step 3: Combine energy charge and fixed charge for the subtotal
subtotal = energy_charge + fixed_charge

# Step 4: Calculate the GST tax amount
gst_amount = (subtotal * gst_percentage) / 100

# Step 5: Calculate the final total bill
total_bill = subtotal + gst_amount

# Step 6: Display the itemized breakdown
print("\n--- Bill Summary ---")
print(f"Energy Charge: {energy_charge:.2f}")
print(f"Fixed Charge:  {fixed_charge:.2f}")
print(f"Subtotal:      {subtotal:.2f}")
print(f"GST ({gst_percentage}%):  {gst_amount:.2f}")
print(f"--------------------")
print(f"Total Bill:    {total_bill:.2f}")