# List and Tuples
# A built-in data type that stores set of values
# It can store elements of different data types
# Lists are mutable (can be changed), Tuples are immutable (cannot be changed)

# List - Ordered, Mutable, Allows Duplicates 
marks = [85, 90, 78, 92]  # List
print(marks) 
print(type(marks)) 
print(marks[0])  # Accessing first element
marks[1] = 95  # Modifying second element
print(len(marks))  # Length of the list
marks.append(88)  # Adding an element at the end 
print(marks)
marks.remove(78)  # Removing an element
print(marks)
marks.pop()  # Removing last element
print(marks)
marks.sort()  # Sorting the list
print(marks) 
marks.sort(reverse=True)  # Sorting in descending order
print(marks)
marks.insert(2, 89)  # Inserting an element at index 2
print(marks)
marks.reverse()  # Reversing the list
print(marks)
print(marks[::-1])  # Reversing the list
print(marks[1:3])  # Slicing the list from index 1 to 2

# Tuple - Ordered, Immutable, Allows Duplicates
fruits = ("apple", "banana", "cherry", )  # Tuple 
print(fruits) 
print(type(fruits)) 
print(fruits[0])  # Accessing first element
print(len(fruits))  # Length of the tuple
# fruits[1] = "orange"  # This will raise an error as tuples are immutable
print(fruits.count("banana"))  # Count occurrences of an element
print(fruits.index("cherry"))  # Finding index of an element