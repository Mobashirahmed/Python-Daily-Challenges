# Personal Information Program

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
height = float(input("Enter your Height (in feet): "))
weight = float(input("Enter your Weight (in kg): "))
city = input("Enter your City: ")

#Display the formatted profile summary
print("\n=== Personal Profile Summary ===")
print(f"Name:   {name}")
print(f"Age:    {age} years old")
print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"City:   {city}")
print("================================")
