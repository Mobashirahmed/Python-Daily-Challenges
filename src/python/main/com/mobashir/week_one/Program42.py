principal = float(input("Please enter the principal: ₹"))
rate = float(input("Please enter the rate: "))
time = int(input("Please enter the time(in years): "))
comp_freq = int(input("Please enter the compound frequency: "))

#Convert percentage rate to decimal
rate = rate/100

#Calculate total accumulated amount (A)
final_amount = principal * ((1 + (rate/comp_freq)) ** (comp_freq * time))

#Calculate interest earned (CI)
interest_earned = final_amount - principal

print(f"Final amount earned: ₹{final_amount:.3f}\n"
      f"Interest earned: ₹{interest_earned:.3f}")