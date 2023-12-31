# Strings, formatting

name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Format placeholders
print("Hello {}, you are {} years old.".format(name, age))  # Hello John, you are 36 years old.

# Format placeholders with indexes
print("{1} years old person, named {0}.".format(name, age))  # 36 years old person, named John.

# Fast string formatting (f-strings)
print(f"Name: {name}, age: {age} years.")  # Name: John, age: 36 years.

# Arbitrary expressions on f-strings
print(f"Score is: {5+15}.")  # Score is: 20.

# Slicing (start:end:step), start-included, end-excluded
str1 = "PythoX"
print(str1[:], str1[::])  # PythoX, slicing parameters not defined, substring is equal to the original
print(str1[:4])  # Pyth, with start parameter not defined, substring starts from the start of the string
print(str1[2:5])  # tho
print(str1[3:])  # honX, with end parameter not defined, substring goes to the end of the string
print(str1[::2])  # PtoX, step goes by 2 each time, from start to the end

# Concatenation and multiplication
firstname, lastname = "John", "Doe"
fullname = firstname + " " + lastname
print(fullname)  # John Doe
print(" ".join([firstname, lastname]))  # John Doe, join method on strings
print(firstname * 2)  # JohnJohn, repetition as multiplication with integer value

# Operations on strings
print(str1.islower())  # False
print(str1.upper())  # PYTHOX
print(str1.lower())  # pythox
print(str1.replace("X", "R"))  # PythoR
print(len(str1))  # 6
print(str1.index("th"))  # 2
print(str1.find("yt"))  # 1
