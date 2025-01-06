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

for e1,e2 in zip(words,stem_words):
 print(e1+' ----> '+e2)


#demo for list
my_list = [1,"hello",2,"reddie","apple"]
print("original list",my_list)
#adding an element to the list
my_list.append("jack")
print("after appending the:",my_list)
#removing an element from the list
my_list.remove('reddie')
print("after removing the:",my_list)
my_list.insert(0,"jack")
print("after inserting the:",my_list)
my_list.append(21)
print("after appending the:",my_list)
middle_index = len(my_list)//2
my_list.insert(middle_index, "middle_index_elemet")
print("after inserting in middle:",my_list)
print("slicing with step(start:stop:step)")
print("0:2:1 slicing",my_list[0:2:1])
print("reverse elements",my_list[::-1])


#tuple operations

my_tuple = (1,'hello',2,'reddie','apple')
print("original tuple",my_tuple)
#accessing elements in the tuple
print("first element :",my_tuple[0])
#accessing last element in the tuple
print("last element:",my_tuple[-1])

#set operations
my_set = {1,2,4,5,6}
print("original set",my_set)
#adding an element to the set
my_set.add(7)
print("after adding the element 7:",my_set)

#dictionary operations 
my_dict = {'name':"raju",'age':25,'city':'newyork'}
print("original dictionary:",my_dict)
#accessing values in the dictionary
print("name:",my_dict['name'])
print("age:",my_dict["age"])
my_dict['age']=21
print("after updating the age:",my_dict)


