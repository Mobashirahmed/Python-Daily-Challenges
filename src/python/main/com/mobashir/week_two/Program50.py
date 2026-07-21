"""
Mini Project – Scientific Arithmetic Calculator

Create a calculator that accepts two numbers and displays:

•Addition
•Subtraction
•Multiplication
•Division
•Floor Division
•Modulus
•Exponentiation

Also display:

•Comparison results (==, !=, >, <, >=, <=)
•Bitwise operations (&, |, ^, ~, <<, >>)
•Demonstrate assignment operators (+=, -=, *=, /=, %=) on one of the numbers
"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

# Perform Arithmetic operations
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {b} = {a**b}\n")

# Comparisons
print(f"Is {a} == {b} ==> {a == b}")
print(f"Is {a} != {b} ==> {a != b}")
print(f"Is {a} > {b} ==> {a > b}")
print(f"Is {a} >= {b} ==> {a >= b}")
print(f"Is {a} < {b} ==> {a < b}")
print(f"Is {a} <= {b} ==> {a <= b}\n")

# Bitwise Operations
print(f"{a} & {b} ==> {a & b}")
print(f"{a} | {b} ==> {a | b}")
print(f"{a} ^ {b} ==> {a ^ b}")
print(f" ~ {a} ==> {~a}")
print(f"{a} << {b} ==> {a << b}")
print(f"{a} >> {b} ==> {a >> b}\n")

# Assignment Operators
a += 6
print(a)
a -= 4
print(a)
a *= 2
print(a)
a /= 3
print(a)
a %= 7
print(a)
a **= 3
print(a)
a //= 2
print(a)