# Student Report Card Generator

student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

print("\nEnter marks obtained out of 100:")
sub1 = int(input("English Marks: "))
sub2 = int(input("Hindi Marks: "))
sub3 = int(input("Science Marks: "))
sub4 = int(input("SSt Marks: "))
sub5 = int(input("Mathematics Marks: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
average_marks = total_marks / 5
percentage = (total_marks / 500) * 100

# Display the final Report Card
print("\n====================================")
print("        OFFICIAL REPORT CARD        ")
print("====================================")
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("------------------------------------")
print(f"English      : {sub1} / 100")
print(f"Hindi        : {sub2} / 100")
print(f"Science      : {sub3} / 100")
print(f"SSt          : {sub4} / 100")
print(f"Mathematics  : {sub5} / 100")
print("------------------------------------")
print(f"TOTAL MARKS  : {total_marks} / 500")
print(f"AVERAGE MARKS: {average_marks:.2f}")
print(f"PERCENTAGE   : {percentage:.2f}%")
print("====================================")