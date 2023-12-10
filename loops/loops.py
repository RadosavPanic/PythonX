# Range, for loop, while loop

# range(start, stop, step)
numbers_list1 = list(range(1, 15, 2))  # [1, 3, 5, 7, 9, 11, 13]
print(numbers_list1)

# For loop with range(stop)
for num in range(5):
    print(num)  # 0 1 2 3 4

# Foor loop with strings
for letter in 'PythonX':
    print(letter)  # P y t h o n X

# While loop -> while [boolean]
counter = 0
while counter < 3:
    print(f"{counter + 1}: Python is great language")
    counter = counter + 1  # will be printed 3 times (0, 1, 2) until 3

# Break (loop control statement)
for letter in 'PythonX':
    if letter == 'o':
        break
    else:
        print(letter)  # P y t h

# Break statement when 50% capacity is reached, otherwise incremented by step of 10
boat_capacity = 500
treshold = boat_capacity * (50.0 / 100.0)
for i in range(0, boat_capacity, 10):
    if i > treshold:
        print("50% capacity reached")
        break
    else:
        print(f"Passengers onboarded: {i}")
