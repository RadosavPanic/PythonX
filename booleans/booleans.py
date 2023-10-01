# Booleans

print(15 > 3)  # True
print(15 == 15.0)  # True

print(bool(1))  # True
print(bool(0))  # False

print(15 > 2 and 15 > 17)  # False (AND logical operator)
print(all([15 > 2, 15 > 17]))  # False (Enforces AND operator)

print(15 > 2 or 15 > 17)  # True (OR logical operator)
print(any([15 > 2, 15 > 17]))  # True (Enforces OR operator)

print(bool(15), not 15)  # True False (NOT logical operator)

print(bool(None))  # False (Null representing value)
