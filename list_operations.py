# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry

# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append("date")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Removing elements
fruits.remove("blueberry")
print(fruits)  # Output: ['apple', 'cherry', 'date']

# List length
print(len(fruits))  # Output: 3

# Slicing a list
print(fruits[1:3])  # Output: ['cherry', 'date']

# Looping through a list
for fruit in fruits:
    print(fruit)

# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
