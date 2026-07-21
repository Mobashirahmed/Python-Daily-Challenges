# Create two variables referring to the same list and verify using the is operator.
list1 = [1, 2, 3]

# Assign list1 to list2 (both now point to the same list)
list2 = list1

# Verify identity using the 'is' operator

print(list2 is list1) # evaluates to True
