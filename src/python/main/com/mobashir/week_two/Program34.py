# Write a program showing the output of different combinations of logical operators on Boolean values.

true = True
false = False

print(f"not {true} ==> {not true}")
print(f"not {false} ==> {not false}")

print(f"{true} and {true} ==> {true and true}")
print(f"{true} and {false} ==> {true and false}")
print(f"{false} and {false} ==> {false and false}")

print(f"{true} or {true} ==> {true or true}")
print(f"{true} or {false} ==> {true or false}")
print(f"{false} or {false} ==> {false or false}")

# Sample boolean variables
a = True
b = False
c = True

# Combination 1: Mixing 'and' with 'or'
# (a and b) evaluates first, then the result is used with 'or c'
comb1 = a and b or c

# Combination 2: Changing order using parentheses
# (b or c) evaluates first, then the result is used with 'a and'
comb2 = a and (b or c)

# Combination 3: Using 'not' with 'and'
# 'not b' evaluates first to True, then 'a and True' evaluates
comb3 = a and not b

# Combination 4: A complex mix of all three
comb4 = (not a or b) and c

# Print the results
print("--- Setup ---")
print(f"a = {a}, b = {b}, c = {c}\n")

print("--- Results ---")
print("1. a and b or c      ->", comb1)
print("2. a and (b or c)    ->", comb2)
print("3. a and not b       ->", comb3)
print("4. (not a or b) and c ->", comb4)