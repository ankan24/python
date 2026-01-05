# Dictionary and Set Operations in Python
# This script demonstrates various operations on dictionaries and sets in Python.
# Dictionary - Unordered, Mutable, Key-Value Pairs
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Science", "History"],
    "marks" : { "Math": 90, "Science": 85},
    24 : "ID Number",
}
empty_dict = {}  # Empty dictionary
print(student)
print(type(student))
print(student["name"])  # Accessing value by key
student["age"] = 22  # Modifying value by key
print(len(student))  # Length of the dictionary
student["grade"] = "A"  # Adding a new key-value pair
print(student)
del student["courses"]  # Removing a key-value pair
print(student)
print(student.get("name"))  # Accessing value using get method # If key doesn't exist, returns None
print(student.keys())  # Getting all keys
print(student.values())  # Getting all values
print(student.items())  # Getting all key-value pairs
student.update({"age": 23, "city": "New York"})  # Updating multiple key-value pairs
print(student)
print(student["marks"]["Math"])  # Accessing nested dictionary value


# Set - Unordered, Mutable, No Duplicates
colors = {1,2,2,"red", "green", "blue"}  # Set
empty_set = set()  # Empty set
print(colors)
print(type(colors))
print(len(colors))  # Length of the set
colors.add("yellow")  # Adding an element
print(colors)
colors.remove("green")  # Removing an element
print(colors)
colors.discard("purple")  # Removing an element if it exists, no error if it does not exist 
print(colors)
colors.pop()  # Removing an arbitrary element 
print(colors)
colors.clear()  # Clearing the set
print(colors)
# Demonstrating set operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(setA.union(setB))  # Union of two sets - all elements from both sets 
print(setA.intersection(setB))  # Intersection of two sets - common elements
print(setA.difference(setB))  # Difference of two sets
print(setA.symmetric_difference(setB))  # Symmetric difference of two sets
print(setA.issubset({1, 2, 3, 4, 5}))  # Check if setA is a subset
print(setA.issuperset({1, 2}))  # Check if setA is a superset
print(setA.isdisjoint({5, 6}))  # Check if setA is disjoint with another set
# Note: Sets do not support indexing or slicing as they are unordered collections. does not exist
print(colors)


# Pairs and Frozensets
# Pair - Immutable ordered collection of two elements
pair = (10, "Ten")
print(pair)
print(type(pair))
print(pair[0])  # Accessing first element
print(pair[1])  # Accessing second element
# pair[0] = 20  # This will raise an error as pairs are immutable
# Frozenset - Immutable version of a set
frozensetA = frozenset([1, 2, 3, 4])
print(frozensetA)
